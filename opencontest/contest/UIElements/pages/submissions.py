from django.http import HttpResponse

from contest import register
from contest.UIElements.lib.htmllib import UIElement, h, h2
from contest.UIElements.lib.page import Card, Page
from contest.models.contest import Contest
from contest.models.submission import Submission
from contest.models.user import User


class SubmissionDisplay(UIElement):
    def __init__(self, submission: Submission):
        subTime = submission.timestamp
        probName = submission.problem.title
        cls = "red" if submission.result != "ok" else ""
        self.html = Card("Submission to {} at <span class='time-format'>{}</span>".format(probName, subTime), [
            h.strong("Language: <span class='language-format'>{}</span>".format(submission.language)),
            h.br(),
            h.strong("Result: <span class='result-format'>{}</span>".format(submission.result)),
            h.br(),
            h.br(),
            h.strong("Code:"),
            h.code(submission.code.replace("\n", "<br/>").replace(" ", "&nbsp;"))
        ], cls=cls)


def getSubmissions(request, *args, **kwargs):
    submissions = []

    cont = Contest.getCurrent()
    if not cont:
        return HttpResponse('')

    user = User.get(request.COOKIES['user'])
    Submission.forEach(
        lambda x: submissions.append(x) if x.user.id == user.id and cont.start <= x.timestamp <= cont.end else None)
    if len(submissions) == 0:
        return HttpResponse(Page(
            h2("No Submissions Yet", cls="page-title"),
        ))
    return HttpResponse(Page(
        h2("Your Submissions", cls="page-title"),
        *map(SubmissionDisplay, submissions)
    ))


# TODO: test
# register.web("/submissions", "loggedin", getSubmissions)
