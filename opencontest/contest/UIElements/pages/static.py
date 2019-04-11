from django.http import HttpResponse

from contest.auth import admin_required
from contest import register
from contest.UIElements.lib.htmllib import div, h2, h, UIElement, h1
from contest.UIElements.lib.page import uuid, Page, Card


@admin_required
def setup(request):
    return HttpResponse(Page(
        h2("Setup", cls="page-title"),
        Card("Problems", "Create problems to go in the contests", "/problems_mgmt"),
        Card("Contests", "Create contests", "/contests"),
        Card("Users", "Create users who will participate in contests, as well as other admin users who can create and judge contests and problems", "/users")
    ))


class FAQ(UIElement):
    def __init__(self, q, a):
        id = str(uuid())
        self.html = div(
            h.h4(q, cls="qa-question collapsed", **{"data-toggle": "collapse", "data-target": f"#qa-{id}"}),
            div(a, id=f"qa-{id}", cls="collapse"),
            cls="faq"
        )

# Fake privacy policy for laughs
register.web("/privacy2", "any", lambda params, user: Page(
        h2("Privacy Policy", cls="page-title"),
        h1("LOL", cls="jumbotron center"),
        h1("After all, you use Facebook", cls="center")
    ))

register.web("/privacy", "any", lambda params, user: Page(
        h2("Privacy Policy", cls="page-title"),
        Card("TL;DR", "OpenContest as an organization is too lazy to steal your data (we're busy enough keeping track of our own). " +
             "However, the organizers of your contest may collect any data you submit, " +
             "including your name (which the organizers provide) and any code submissions, which they may use for any purpose."),
        Card("Data collected",
             div(
                h.span("OpenContest collects the following data:"),
                h.ul(
                    h.li("Your name as provided by the contest organizers"),
                    h.li("Your password as generated by the app"),
                    h.li("Any problem statements written by the contest organizers"),
                    h.li("Any contest details created by the contest organizers"),
                    h.li("Any code submissions by contest participants")
                )
             )),
        Card("Data usage",
             div(
                h.span("Any data collected by OpenContest may be accessible to"),
                h.ul(
                    h.li("The contest organizers"),
                    h.li("Anyone with access to the server that OpenContest is running on"),
                    h.li("Anyone in the world, though we have tried to eliminate this possibility")
                ),
                h.span("Any data collected in OpenContest is stored in plain text on the server that OpenContest is running on. " +
                       "No data is not sent to the developers of OpenContest.")
             ))
    ))


    # Instructions about using OpenContest
register.web("/faqs", "any", lambda params, user: Page(
        h2("FAQs", cls="page-title"),
        FAQ("What is a programming contest?", """A programming contest is a contest where programmers 
            attempt to solve problems by writing programs. These problems are typically posed as a 
            problem statement to describe the problem, input that the program must process, and 
            output that the program must produce. The goal of solving the problem is to write a 
            program that produces the same output for a given input as the judge's solution."""),
        FAQ("What happens when I submit code for a problem?", """When you submit code for a problem, 
            your code is automatically run against secret test data and judged based on the output
            it produces. Your code can recieve the following verdicts:
            <ul><li><i>Accepted</i>: Your code produced the correct output for all test cases.</li>
                <li><i>Wrong Answer</i>: Your code produced incorrect output for some test case.</li>
                <li><i>Runtime Error</i>: Your code threw an exception and exited with a non-zero exit code.</li>
                <li><i>Time Limit Exceeded</i>: Your code ran longer than the time allowed.</li></ul>
            """),
        FAQ("How does scoring work?", """Your score is determined by two factors: the number of problems 
            you solve and the number of penalty points you accrue. Contestants are ranked first on 
            problems solved and then on penalty points. A contestant who solves 5 problems will always
            rank higher than a contestant who solves 4 problems, but two contestants 
            who each solve 4 problems will be ranked against each other by penalty points.<br/><br/>
            Penalty points are determined by the time it takes you to solve the problems and the number 
            of incorrect submissions that you make. When you solve a problem, you accrue 1 penalty point 
            for each minute that has elapsed from the beginning of the contest and 20 penalty points 
            for each incorrect submission you made to that problem. For example, if you solve a problem 
            137 minutes into the contest after making 2 incorrect submissions, you will accrue 177 
            penalty points. You do not accrue penalty points for incorrect submissions to a problem 
            if you never solve that problem.<br/><br/>
            For example, if Jim and Bob solve problems at the following times,<br/><br/>
            <table>
                <thead><tr><th>Problem</th>
                    <th class="center">1</th><th class="center">2</th><th class="center">3</th>
                    <th class="center">4</th><th class="center">5</th></tr></thead>
                <tbody>
                    <tr><td>Jim</td>
                        <td class="center">37 minutes,<br/>1 wrong<br/>57 points</td>
                        <td class="center">14 minutes,<br/>2 wrong<br/>54 points</td>
                        <td class="center">43 minutes,<br/>0 wrong<br/>43 points</td>
                        <td class="center"><br/>5 wrong<br/>0 points</td>
                        <td class="center">59 minutes,<br/>1 wrong<br/>79 points</td>
                    </tr>
                    <tr><td>Bob</td>
                        <td class="center">7 minutes,<br/>0 wrong<br/>7 points</td>
                        <td class="center">23 minutes,<br/>1 wrong<br/>43 points</td>
                        <td class="center"><br/><br/>0 points</td>
                        <td class="center">53 minutes,<br/>2 wrong<br/>93 points</td>
                        <td class="center">41 minutes,<br/>1 wrong<br/>61 points</td>
                    </tr>
                </tbody>
            </table><br/>
            Jim will receive a total of 233 points, and Bob will receive a total of 204 points.
            Since Bob has fewer penalty points, he will rank above Jim.
            """),
        FAQ("Where can I find information about my language?", """There is language documentation available for the following languages:
            <ul><li><a target="_blank" href="https://en.cppreference.com/w/c/language">C</a></li>
                <li><a target="_blank" href="https://en.cppreference.com/w/">C++</a></li>
                <li><a target="_blank" href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/">C#</a></li>
                <li><a target="_blank" href="https://docs.oracle.com/javase/8/docs/api/">Java</a></li>
                <li><a target="_blank" href="https://docs.python.org/2/library/">Python 2</a></li>
                <li><a target="_blank" href="https://docs.python.org/3/library/">Python 3</a></li>
                <li><a target="_blank" href="https://ruby-doc.org/stdlib-2.5.3/">Ruby</a></li>
                </ul>"""),
        FAQ("What compiler flags are being used?", """The following languages are compiled with non-default compiler flags:
            <ul><li>C: -std=c11 -O2</li>
                <li>C++: -std=c++17 -O2</li>
                </ul>"""),
        FAQ("Why am I getting the Wrong Answer verdict?", """There are several reasons you could be getting Wrong Answer, but here are the two of the most common:
            <ul><li>Your output formatting does not match the judge's. Output formatting must exactly match.</li>
                <li>Your method of solving the problem is incorrect.</li>
                </ul>"""),
        FAQ("Why am I getting the Runtime Error verdict?", """There are several reasons you could be getting Runtime Error, but here are a few of the most common:
            <ul><li>Your code divided by zero or took the square root of a negative number.</li>
                <li>Your code read or wrote to an array at an index that was out of bounds.</li>
                <li>Your C/C++ code dereferenced an invalid pointer, such as nullptr or a pointer to an object that had been deleted.</li>
                <li>Your Java code called a method on a null object.</li>
                <li>Your Python code exceeded Python's recursion depth limit. Python allows only a few hundred recursive calls to a function.</li>
                <li>Your C/C++ code failed to return 0 from the main function.</li>
                </ul>"""),
    ))