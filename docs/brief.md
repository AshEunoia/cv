<!-- 2026-11-13-01-27-36 -->
# CV brief

What Ash Eunoia's CV is for, who reads it, the principles it follows and what goes in it. Written on 13 November 2026, when the CV moved from Word to Markdown. Update this file when a decision changes.

This repository is public, so this brief holds nothing private: no health details beyond what the CV itself says, no salary expectations, and no other people's contact details. Private material, such as Ash's notes, cover letters and the copies sent to employers, stays in Ash's private SVN repository.

## Goal

The CV gets Ash shortlisted for software developer jobs: past the first filters, human and automated, and into an interview or assessment. It doesn't need to get Ash the job by itself. That's the job of the interview, and of the portfolio behind it. CODE Cumbria's CV session put it the same way: the goal "is not to get you a job but to pass the initial filters to get to the next stage" (Ash's notes, October 2025).

It also sets up the next steps a reader takes. A hiring manager who likes the CV opens LinkedIn, then GitHub or kyberfex.com, so all of them should tell the same story.

## Audience

Employers hiring software developers, for **remote work, or work in or near Cockermouth**. Ash's strongest evidence is in web development (Python with Django and Wagtail, and TypeScript with Astro on Square's APIs), so web developer roles fit too. Clients aren't the audience: they have [kyberfex.com](https://kyberfex.com/). The CV is linked from the site's About page, though, so a client may read it, and its tone should match the site's.

Four kinds of reader, in the order they meet the CV:

1. **Screening software.** An applicant tracking system, and more and more often an AI screening step, reads the text and matches it against the advert. It needs plain, machine-readable text and the advert's own words.
2. **A recruiter,** in-house or at an agency, who gives it a first look of a few seconds. In Ladders' eye-tracking study the first pass averaged 7.4 seconds, spent on job titles, employers, dates and keywords ([Ladders, 2018](#sources)).
3. **The hiring manager,** often a developer or team lead, who reads it properly and decides whether to click through to the work. They look for evidence that Ash ships working software, tests it, and works well with people.
4. **The interviewers,** who use it to choose their questions. Every claim should be something Ash can talk about with an example.

## Terms

**Call it a CV.** In British English, "CV" (short for curriculum vitae) is the usual word for the document sent with a job application. "Résumé" is the American and Canadian word. In the US, "CV" mostly means the longer academic version ([Cambridge Dictionary](#sources); [Prospects](#sources)). So the document, the file names, the repository (`AshEunoia/cv`, renamed from `resume`) and its README say "CV". "Résumé" appears only where it helps people searching with the American word find it: once in the README, in the repository's description, and as one of its topics.

## Principles

The UK sources (Prospects and the National Careers Service) set the conventions. The American sources (Bock and the Tech Interview Handbook) are used only for how to write achievements, because American résumé conventions, such as a strict one-page limit, differ from British ones.

1. **Two A4 pages at most, and one if it fits.** Prospects recommends "no longer than two A4 pages", and CODE Cumbria's session said one page is ideal and two the maximum. Summarise old details, such as school grades, rather than listing them ([Prospects](#sources)).
2. **The name is the title.** Don't head the document "Curriculum vitae" or "CV" ([Prospects](#sources)).
3. **Contact details, and nothing personal.** Name, phone number, email, LinkedIn, and the website or portfolio ([National Careers Service](#sources); [Prospects](#sources)), plus GitHub ([Tech Interview Handbook](#sources)). Leave out age, date of birth, marital status and nationality ([National Careers Service](#sources)), and a photo ([Prospects](#sources)). On a copy posted online, leave out the home address, because "you could be targeted by fraudsters" ([Prospects](#sources)), so give the town only: Cockermouth, Cumbria. Ash's phone number is public already, so it stays on the public copy.
4. **A short personal statement at the top.** "A few short lines" on who Ash is and what Ash wants to do ([National Careers Service](#sources)), focused on the sector being applied to ([Prospects](#sources)). It's the part to tailor most for each application: who Ash is, what Ash is aiming for, what Ash is doing to get there, and the core skills that matter for that job (CODE Cumbria).
5. **Experience before education, most recent first.** With relevant work experience, work history comes before education ([Prospects](#sources); [National Careers Service](#sources)).
6. **Achievements, not duties.** Use active verbs and concrete evidence instead of phrases like "team player" ([Prospects](#sources)). Where possible, write each achievement as "accomplished [X] as measured by [Y] by doing [Z]" ([Bock](#sources)), with a number when there is one ([Tech Interview Handbook](#sources)). The approved Jennings bullets already do this.
7. **Easy to scan.** Job titles in bold, with employers and dates easy to find, since those get the first look. Bold titles above bulleted achievements did best in Ladders' study ([Ladders](#sources)). The CV should look clear at a glance too, even zoomed out (CODE Cumbria).
8. **Readable by machines.** Text only, with no images, logos or graphics ([Prospects](#sources)). Use one column and standard section headings with no symbols in them ([Tech Interview Handbook](#sources)). Test it by pasting the PDF's text into a plain text file to check nothing is missing, broken or out of order ([Tech Interview Handbook](#sources)); the build does this on every run.
9. **Tailored to each advert.** Use the keywords in the job description and person specification ([Prospects](#sources); [National Careers Service](#sources)), but don't stuff them in, because a person reads it too ([Tech Interview Handbook](#sources)). Spell out abbreviations at least once.
10. **Links to the work.** Link the portfolio, and link each project to its code ([Tech Interview Handbook](#sources)). CODE Cumbria's session stressed that a good portfolio counts for a lot, if the hiring manager clicks through.
11. **References on request.** Don't list referees' contact details. Say references are available on request ([National Careers Service](#sources)), or leave the line out if space is tight ([Prospects](#sources)). Ash's Jennings reference is offered on request, and Ash checks with the referee before passing on their details.
12. **Gaps, honestly and briefly.** Give the dates and a brief reason, without personal detail, and show what was done in the time, such as courses, projects or volunteering ([Prospects](#sources)). Ash chose to show the gaps: the career break from late 2023 to mid-2025 is on the CV, "for health reasons", and nothing more.
13. **Every claim checkable.** Only claim what Ash can back with an example at interview, using the STAR method (situation, task, action, result) ([National Careers Service](#sources)). Name things instead of counting them: list the languages rather than "over 10 programming languages".
14. **Say how the work is done.** Ash builds software with Claude Code, an AI coding assistant: planning the work, reviewing what it writes and checking it with automated tests. The CV says so plainly, as kyberfex.com does, and puts the languages in the context of that work. Ash should expect technical interviews to probe it, including tests that ask for code written without the assistant *(judgement)*.
15. **Jennings in its approved wording only.** The brewery approved specific wording, which leaves out customers, supplier names and figures beyond those in it. Use the approved short version, kept with the website project's content, changing only the tense now that the contract has ended.
16. **The same story everywhere.** Titles, dates and descriptions match kyberfex.com and LinkedIn.
17. **Plain English, British spelling.** Short sentences with no filler: "brutally concise text, no wasted or redundant words" (CODE Cumbria). Use British spelling throughout ("modelling", "organisation").
18. **Readable type.** Body text at 10 to 12 point (11 here), headings at 14 to 16 point in bold, one consistent style, and margins of about 2.5 cm ([Prospects](#sources); [National Careers Service](#sources)).
19. **An accessible PDF** *(judgement)*: selectable text, a tagged structure so screen readers and parsers read it in the right order, bookmarks for the sections, the language set to British English, and the document's title set to Ash's name.

## Content

### Where it comes from

- **The Word CV** of April 2026 (`resume-ash-eunoia-tech.docx`, kept in this repository's history and in SVN): the library job, the HNC and school, and computer support since 2022.
- **The care version** (deleted, still in SVN's history): the cleaning job at Cockermouth Banking Hub, July 2025 to April 2026.
- **An older general CV** from May 2025 (SVN only): more on the library job, such as the Koha records and the training documentation.
- **Jennings Brewery's approved wording,** kept with the website project's content.
- **kyberfex.com's portfolio:** this website, Blender Asset Remap and the Dymaxion projector.
- **CODE Cumbria's certificate of achievement** (12 December 2025) and its onboarding pack: an 11-week Skills Bootcamp, from 23 September to 10 December 2025, in Whitehaven and online, for tech roles in the nuclear, energy and engineering sectors.
- **Meridiana Creative's website,** from Ash's private repository for it: a client site Ash designed and built in Wagtail in November 2026, not yet launched. Ash has the client's permission to show it. The CV names the business only, not its owner or anyone in its copy.
- **Ash's answers** of 13 November 2026: Kyberfex dates from 14 April 2026, when Ash bought kyberfex.com; Python is the main language.

### What changed from the Word CV

- **Added:** Jennings Brewery, Kyberfex with its client work for Meridiana Creative, the projects, a GitHub link, and the skills by name.
- **Reframed:** the headline and profile point at software development, not database and network administration. The library job is told as projects (the move to Excel and VBA, the training documentation, the records).
- **Corrected:** CODE Cumbria's dates, which read "September – March 2025"; "Lead a team" to "Led"; American spellings; and "Cockermouth, England" to "Cockermouth, Cumbria".
- **Cut:** the generic summary ("versatile", "unique blend", "leverage", "drive innovation"), the unnamed "over 10 programming languages", the abbreviated grades, and the creative tools other than Blender, to keep to two pages.

### Structure

1. **Name, headline and contact line:** "Software developer · Python, Django and TypeScript", then town, phone, email, LinkedIn, GitHub and kyberfex.com.
2. **Profile:** four or five lines, tailored to each application.
3. **Experience,** most recent first: Kyberfex (Meridiana Creative's website, kyberfex.com, and computer help); Jennings Brewery; the cleaning job and the career break, one line each; and the library job.
4. **Projects:** Blender Asset Remap and the Dymaxion projector, each title linked to its code. The website is under Kyberfex.
5. **Skills:** languages, frameworks and services, databases, and how Ash works. Only what the experience above backs up.
6. **Education and training:** the CODE Cumbria Skills Bootcamp, the HNC, and school in one entry.
7. **Interests,** one line, then "References are available on request."

## Format and build

- **One Markdown file,** `cv.md`, is the source. No Word file. If an application insists on Word, because not every applicant tracking system accepts PDFs ([Prospects](#sources)), Pandoc can make one from the same Markdown.
- **`build.py`,** run with uv, turns the Markdown into an HTML page styled by `cv.css`, then prints it to an A4 PDF, `Ash-Eunoia-CV.pdf`, with Playwright's Chromium (Microsoft Edge on Ash's machine). The PDF is tagged, has a bookmark for each section and entry, and is titled with Ash's name.
- **The typeface** is Bricolage Grotesque, as on kyberfex.com, with the site's ink and deep teal. Chromium prints a variable font as Type 3 glyphs, which some parsers read badly, so the build makes fixed instances of the weights it uses and prints with those.
- **Each entry stays on one page:** the build wraps every job, project and qualification, from its title to the next heading, so the page break falls between entries, never inside one.
- **Checks on every build:** it fails if the PDF runs past two pages, if the typeface didn't load, or if the PDF's text differs from the page's, word for word and in order. `--links` also checks every link. LinkedIn and Blender's code site turn automated checks away, so those two are listed to check by hand.
- **The built PDF is committed,** so the README can link to it for anyone arriving from kyberfex.com.

## Version control

- **Git, public:** this repository, at `E:\git\cv` and [github.com/AshEunoia/cv](https://github.com/AshEunoia/cv). It holds the CV, its build, and this brief. It moved out of the SVN working copy on 13 November 2026, with its history.
- **SVN, private:** Ash's employment repository keeps everything private: notes from CODE Cumbria and coaching, cover letters, the dated copies sent to employers, and the old Word CVs, in `trunk/resume`.

## Decisions

| Date | Decision |
| --- | --- |
| 13 November 2026 | Call it a CV, the British term, not a résumé. Rename the repository to `cv`, keeping "résumé" only where it helps searches. |
| 13 November 2026 | One CV, for software development. The care version is deleted (still in SVN's history). |
| 13 November 2026 | Aimed at employers, not clients: remote roles, or roles in or near Cockermouth. |
| 13 November 2026 | Markdown source, with a script to build the PDF; no Word file. |
| 13 November 2026 | Git for the CV, public, in `E:\git\cv`; SVN for private material. |
| 13 November 2026 | Show the gaps. The career break gets one line, "for health reasons"; the cleaning job gets one line. |
| 13 November 2026 | Kyberfex dates from 14 April 2026, when Ash bought kyberfex.com. Python is the main language. The phone number stays on the public copy. |
| 13 November 2026 | Meridiana Creative's website goes under Kyberfex, with the client's permission, and on kyberfex.com's portfolio too. |
| 13 November 2026 | Ash approved the first Markdown version: CODE Cumbria's dates, the career break, the profile's account of working with Claude Code, and "Software developer" for the Kyberfex entry. |

## Open questions for Ash

1. **Meridiana Creative's link:** add meridianacreative.com to its entry once the site is live.
2. **2012 to 2016:** the years between the HNC and the library job are shown as a gap with no entry. Is there anything worth a line?
3. **Extras:** a driving or motorcycle licence, first aid, or other certificates worth a line?
4. **LinkedIn:** update it to match the CV, as the employment coach suggested?
5. **The SVN folder** `trunk/resume` still has "resume" in its name. Rename it, for example to `cv-word`, or leave the archive as it is?

## Sources

Checked on 13 November 2026.

- **Cambridge Dictionary:** [CV](https://dictionary.cambridge.org/dictionary/english/cv) ("mainly UK", "US usually résumé") and [résumé](https://dictionary.cambridge.org/dictionary/english/resume) ("US", "UK CV").
- **Prospects:** [How to write a CV](https://www.prospects.ac.uk/careers-advice/cvs-and-cover-letters/how-to-write-a-cv), by Jemma Smith, May 2025. Prospects is Jisc's graduate careers service.
- **National Careers Service:** [How to write a CV](https://nationalcareers.service.gov.uk/careers-advice/cv-sections), the government's careers service for England.
- **Bock:** Laszlo Bock, then Google's head of People Operations, [My Personal Formula for a Winning Resume](https://www.linkedin.com/pulse/20140929001534-24454816-my-personal-formula-for-a-better-resume), LinkedIn, 29 September 2014.
- **Ladders:** [Eye-Tracking Study](https://www.prnewswire.com/news-releases/ladders-updates-popular-recruiter-eye-tracking-study-with-new-key-insights-on-how-job-seekers-can-improve-their-resumes-300744217.html), November 2018. It's a US study, and Ladders doesn't say how many recruiters took part, so treat the 7.4 seconds as a rough guide.
- **Tech Interview Handbook:** [Practical guide to writing FAANG-ready software engineer resumes](https://www.techinterviewhandbook.org/resume/), updated 7 August 2026. It's American (it says one page), so it's used here only for how to write achievements and skills.
- **Playwright:** [`page.pdf()`](https://playwright.dev/python/docs/api/class-page#page-pdf), for tagged PDFs with bookmarks.
- **CODE Cumbria's CV and cover letter sessions,** and an employment coaching session: Ash's own notes from 2025, not published.
