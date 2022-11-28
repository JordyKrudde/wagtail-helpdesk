from django.template.response import SimpleTemplateResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from wagtail_helpdesk.cms.models import Answer, AnswerCategory
from wagtail_helpdesk.core.forms import (
    ClimateQuestionForm,
    ClimateQuestionUserContactForm,
)
from wagtail_helpdesk.core.models import Question


class AskAQuestionPage(FormView):
    """
    This is the page where users can submit a new question. It consists of a form
    that is spread over two steps using JavaScript.
    """

    template_name = "core/ask_a_question_page.html"
    form_class = ClimateQuestionForm
    success_url = reverse_lazy(
        "core:post-question"
    )  # Forward with POST to the other view

    def get_random_category_and_questions(self):
        """
        We can use order by ? since its only 9 items.
        Suggested category with answers.
        """
        categories = AnswerCategory.objects.filter(
            category_answer_relationship__answer__live=True
        ).distinct()
        random_category = categories.order_by("?").first()
        answers = (
            Answer.objects.live()
            .specific()
            .filter(
                answer_category_relationship__category=random_category, type="answer"
            )
        )

        return {
            "category": random_category,
            "answers": answers,
        }

    def get_questions_per_category(self):
        """
        Retrieve all and filter in JS later.
        """
        result = {}
        categories = AnswerCategory.objects.filter(
            category_answer_relationship__answer__live=True
        ).distinct()
        for category in categories:
            answers = (
                Answer.objects.live()
                .specific()
                .filter(answer_category_relationship__category=category, type="answer")
                .distinct()
            )
            if answers:
                category_class = str(category).replace(" ", "_")
                result[category_class] = {"answers": answers, "name": str(category)}
        return result

    def get_context_data(self, **kwargs):
        """
        Add the random item we retrieved. Form is handled automagically since
        this is a FormView subclass.
        """
        context = super(AskAQuestionPage, self).get_context_data(**kwargs)
        context.update(
            {
                # 'suggestion': self.get_random_category_and_questions(),
                "suggestion_categories": self.get_questions_per_category()
            }
        )
        return context

    def post(self, request, *args, **kwargs):
        """
        We need access to the request object, so we do things here in post rather
        than in the form_valid method.
        """
        form_data = request.POST

        if form_data:
            form = ClimateQuestionForm(form_data)

            if form.is_valid():
                q = Question.objects.create(
                    question=form.cleaned_data["main_question"],
                    relevant_location=form.cleaned_data["relevant_location"],
                    relevant_timespan=form.cleaned_data["relevant_timespan"],
                    extra_info=form.cleaned_data["extra_info"],
                    categories=f"{form.cleaned_data['categories']}",
                    asked_by_ip=self.request.META.get("REMOTE_ADDR"),
                )

                # Store pk in cookies for next form
                request.session["question_id"] = q.pk
                return super(AskAQuestionPage, self).form_valid(form)

            else:
                return super(AskAQuestionPage, self).form_invalid(form)

        return super(AskAQuestionPage, self).form_invalid(ClimateQuestionForm())


ask_a_question_page = AskAQuestionPage.as_view()


class PostQuestionSubmitPage(FormView):
    form_class = ClimateQuestionUserContactForm
    template_name = "core/question_submitted.html"
    success_url = reverse_lazy("core:new-question-thanks")

    def post(self, request, *args, **kwargs):
        """
        We need access to the request object, so we do things here in post rather
        than in the form_valid method.
        """
        form_data = request.POST
        if form_data:
            form = ClimateQuestionUserContactForm(form_data)

            # Update the question with the email
            if form.is_valid():
                question_id = request.session.get("question_id")
                try:
                    question = Question.objects.get(pk=question_id)
                # This should be exceedingly rare, but just in case :D
                except Question.DoesNotExist:
                    return SimpleTemplateResponse("core/new_question_failure.html")
                else:
                    question.user_email = form.cleaned_data["user_email"]
                    question.save()
                    request.session["question_id"] = None

                return super(PostQuestionSubmitPage, self).form_valid(form)
            else:
                return super(PostQuestionSubmitPage, self).form_invalid(form)

        return super(PostQuestionSubmitPage, self).form_invalid(
            ClimateQuestionUserContactForm()
        )


post_question_submit_page = PostQuestionSubmitPage.as_view()
