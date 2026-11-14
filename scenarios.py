"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# ── Text sets ────────────────────────────────────────────────────────────────
# Kept as named lists because criteria 2 and 3 share some of them.

# Criterion 1: ten pieces I wrote myself, no AI help, 100–300 words each.
# At least 3 must be plain: average sentence length of 15 words or fewer.
MY_WRITING_C1 = [
    """
    It has been a interesting jurney for me in a sense coming from Nepal on 2007 and living in United States. 
    For the most part I feal I learn and got alot of opportunity that I might have not gotten if I were in Nepal.
    At the same time I feel like I have missed out alot.
    """,

    """
    I experiences alot of culture different living in United States, and Nepal and visiting in China. 
    One of the big thing I release is in Nepal or China especially in small town or villages neighbors and family are
    very close, they visit each other and help when one needed. Here in US, neighbors hardly know and talk with
    each other.
    """,

    """
    We live in the age of AI. I myself have been studying and using AI for a while but I am also 
    very worried about the future of my employment and in some occasions I felt little 
    depressed about my future career. Well uncertainty makes our lifes both fun and bit scary. 
    """,

    """
    Sequence based machine learning approaches for 1-D and 2-D protein structure prediction 
    tasks have long been limited by relatively small datasets, namely proteins with experimentally
    determined structure. Recent advances in machine learning provide a means of using unlabeled 
    data and, as a result, this opens up access to a much larger sequence space in the context 
    of protein structure prediction
    """,

    """
    Thank you so much for giving me the opportunity; 
    I don't think I will be in Mt. Pleasant anytime soon. On 23rd of January 
    I am moving from Wisconsin to California and start a new Job. If there is 
    a way I can talk with the class through online sometime in April, I will be 
    happy to do that. But if I need to be in classroom I am afraid I can make 
    it this semester. 
    """,

    """
    I just write these scripts for counting words. I will try to find one assignment
    where it requires student to create multiple tables and do some queries using python and MySQL.
    """,

    """
    I hope you are doing good. I am writing this email to check to see if you have everything you need 
    from me for the application. When I check my application status it says waiting for documents, 
    I am wondering if I have to submit any other document.  Thank you for your help, I appreciate it. 
    """,

    """
    Evaluation of the Big Data and its challenges has led to the invention of different tools and methods 
    to solve the problem of Big Data management and analysis. In order to learn from the data one needs to 
    go through the process of knowledge discovery, which includes data collecting, data cleaning, data mining, 
    generating knowledge based on the extracted information of the data mining and, finally, using the learned 
    knowledge for further analysis. Scientists in different domains are forced to develop different tools and 
    methods to handle and analyze these large data sets. One of the goals in data mining is to be able to use 
    large amounts of data and analyze it by using various Machine Learning techniques, to extract useful information. 
    In this work, I am focusing on managing and extracting meaning from large amounts of data by using sets of tools 
    that are being used in many areas to achieve state-of-the-art results in various classification tasks.
    """,

    """
    I am interested on the Software Developer position and
    like to have an interview. On the email you mention about 
    the materials to look at prior to the interview, could you please 
    provide me those and schedule for an interview. Thank you very much. 
    I do appreciate it. Looking forward to hear from you.
    """,

    """
    I hope you are having a good holiday day break.  
    I have enclosed my resume with this email. 
    Thank you so much for you help and support. 
    I really appreciate it. Happy New Year to you and your family.  
    Thank you once again very much.   
    """
]

# Criterion 2 human set: five more of my own unedited pieces, NOT reused from
# criterion 1. Criterion 3 reuses these as its five human inputs.
MY_WRITING_C2 = [
    "I will like to submit my thesis to College of Graduate Studies for further process. "
    "I have included my thesis (Microsoft Word document), Contact Information & Student "
    "Verification Form, Plan A Completion Sign-off Form, and Committee Chair & "
    "Student Verification Form.",

    "It's been a 11 years since Nepal had a major earthquick happend. "
    "Still there is no major changes done, in terms to regulate the building permit in "
    "major city like Kathmandu, which is densely populated and if such a event happens again "
    "there will be many more casualties. I hope the new goverment ran by young generation "
    "will take this matter seriously and put forth some meaningfull strict regulations.",

    "I think traffic in Nepal is bad, I felt same as in bay area, To go to distanct of 15miles specially "
    "in office time, it leterally takes almost 2 hours. I sometime don't understand why "
    "company are against working from home. I think it makes more sense to work from home. "
    "When I work from home, I can start earler then I am suppose to start since I don't have to drive "
    "and I am right in my home office. And alos I tends to work late since I don't "
    "have to leave office and drive back home.",

    "One of the best part of living in Marquette Michigan is the outdoors activities. "
    "I got to live in Marquette for more then 5 years and I loved it. "
    "In summer and winter both you can do trial ride. Now people aks me wait a minute, "
    "winter time mountain bike ride, yes in Marquette some of the mountain bike trails are "
    "groomed just for flat or mountain bike ride. Its awesome, So different experience "
    "then riding in the summer time. Apart from mountain biking, road riding it has beautful winter "
    "so people do cross country skiing, down hill skiing, snow boarding, as well as big part is "
    "snow shoeing. ",

    "Some time I think of the places I never vistied but I have seen in tv and heard from other focks "
    "Fact is some of them I might get chance to visit in fucture but some "
    "I will never get chance to go."
]

# Criterion 2 AI set, unedited. Criterion 3 reuses these as its five AI inputs.
# Model: Claude Opus 5.5 (claude-opus-5-5). Prompt above each text.
AI_UNEDITED = [
    # Prompt: "Write a short paragraph on why sleep matters for college students."
    "Sleep plays a crucial role in the academic success and overall well-being of "
    "college students. During sleep, the brain consolidates memories, transforming "
    "the information learned throughout the day into long-term knowledge. Without "
    "adequate rest, students often struggle with concentration, problem-solving, and "
    "emotional regulation, which can significantly impact their performance in the "
    "classroom. Furthermore, chronic sleep deprivation has been linked to a weakened "
    "immune system, increased stress levels, and a higher risk of anxiety and "
    "depression. Many students sacrifice sleep to meet deadlines or socialize, but "
    "this trade-off frequently backfires, leading to lower grades and diminished "
    "productivity. By prioritizing a consistent sleep schedule of seven to nine hours "
    "per night, students can enhance their cognitive abilities, maintain better "
    "physical health, and approach their studies with renewed energy and focus. "
    "Ultimately, good sleep is not a luxury but a fundamental foundation for success.",

    # Prompt: "Write a short paragraph about the benefits of learning a second language."
    "Learning a second language offers a wide range of benefits that extend far "
    "beyond the ability to communicate with others. Research has shown that "
    "bilingual individuals often demonstrate improved cognitive flexibility, "
    "stronger problem-solving skills, and enhanced memory. Additionally, learning "
    "a new language opens doors to diverse cultures, allowing individuals to gain a "
    "deeper understanding of different perspectives, traditions, and ways of life. "
    "In today's interconnected world, multilingualism is also a valuable asset in "
    "the job market, as many employers seek candidates who can engage with "
    "international clients and partners. Moreover, the process of learning a "
    "language fosters patience, discipline, and resilience, as learners navigate "
    "challenges and celebrate their progress. Whether for personal growth, career "
    "advancement, or travel, acquiring a second language is a rewarding endeavor "
    "that enriches both the mind and the spirit.",

    # Prompt: "Write a short paragraph on how remote work has changed the workplace."
    "Remote work has fundamentally transformed the modern workplace, reshaping how "
    "organizations operate and how employees approach their careers. With the rise "
    "of digital collaboration tools, teams can now communicate and coordinate "
    "seamlessly across different cities, time zones, and even continents. This "
    "shift has provided employees with greater flexibility, allowing them to achieve "
    "a healthier work-life balance and eliminate time-consuming commutes. At the "
    "same time, companies have gained access to a broader talent pool, no longer "
    "limited by geographic boundaries. However, remote work also presents unique "
    "challenges, including feelings of isolation, difficulties in maintaining "
    "company culture, and the blurring of boundaries between professional and "
    "personal life. As a result, many organizations are adopting hybrid models that "
    "combine the benefits of remote and in-office work. Overall, remote work has "
    "redefined what it means to be productive in the twenty-first century.",

    # Prompt: "Write a short paragraph explaining why recycling is important."
    "Recycling is an essential practice that plays a vital role in protecting the "
    "environment and conserving natural resources. By recycling materials such as "
    "paper, plastic, glass, and metal, we reduce the amount of waste that ends up in "
    "landfills and incinerators, which in turn helps decrease pollution and "
    "greenhouse gas emissions. Recycling also conserves valuable raw materials, "
    "reducing the need for mining, logging, and drilling, activities that can cause "
    "significant harm to ecosystems and wildlife habitats. In addition, the "
    "recycling industry creates jobs and supports local economies, contributing to "
    "a more sustainable future. While recycling alone cannot solve all "
    "environmental challenges, it represents a simple yet powerful action that "
    "individuals and communities can take every day. By making recycling a habit, "
    "we can collectively contribute to a cleaner, healthier planet for future "
    "generations.",

    # Prompt: "Write a short paragraph about the importance of reading for children."
    "Reading is one of the most valuable activities for children's development, "
    "offering benefits that extend well beyond the classroom. When children read "
    "regularly, they build essential language skills, expand their vocabulary, and "
    "improve their comprehension abilities. Reading also sparks imagination and "
    "creativity, allowing young minds to explore new worlds, ideas, and "
    "perspectives. Furthermore, stories help children develop empathy by exposing "
    "them to characters with different experiences, emotions, and backgrounds. "
    "Establishing a reading habit early in life can foster a lifelong love of "
    "learning and contribute to stronger academic performance across all subjects. "
    "Parents and educators play a crucial role in this process by providing access "
    "to engaging books and modeling positive reading behaviors. Ultimately, "
    "encouraging children to read is an investment in their intellectual, "
    "emotional, and social growth that will serve them throughout their lives.",
]

# Criterion 3: the five AI_UNEDITED texts, rewritten BY ME by hand — change
# about half the sentences into my own words. Same order as AI_UNEDITED.
AI_REWRITTEN_BY_ME = [
    "One of the most important things that we college students "
    "needs is good night sleep. It helps us stay focuse and alert in the class rooms. "
    "Study have suggested that students who get enough sleep are "
    "more likely perform better in class and have better memory retention. "
    "On the other hand students who are sleep deprived often struggle with concentration, "
    "problem-solving, and emotional regulation, which can significantly impact their performance in the "
    "classroom.",

    "Its not easy to learn a second language, but it has many benefits. "
    "Learning a new language allows us to communicate with people from different cultures and backgrounds. "
    "Go vist to different countries and learn their language can be a very enriching experience. ",

    "Researchers at Binghamton University are investigating the advantages "
    "and challenges of remote-work practices from different angles, leaning "
    "into their expertise in areas such as leadership development or navigating complex systems. "
    "Keenly aware that students are entering a workforce with new expectations about the dynamics of office life."
    "The most obvious benefit of a virtual work environment is enhanced flexibility. "
    "It has improved accessibility for employees by reducing travel and encouraging a healthier "
    "work–life balance, says Hiroki Sayama, distinguished professor of systems science and industrial "
    "engineering and an expert on complex group dynamics."

    "Recycling and using recycled material is good for manufacturers, consumers, "
    "and the planet. It not only protects the environment, but also strengthens "
    "the economy. When we recycle, we use less of the Earth’s finite resources, "
    "less energy to extract and process virgin materials, and create jobs in a growing industry.",

    "I found the article on importaince of reading for children very interesting. "
    "Young children whose parents read them five books a day enter kindergarten having "
    "heard about 1.4 million more words than kids who were never read to, a new study found."
]


# Names must differ in their first 12 characters: run_eval.py builds each
# creator_id from name[:12], and a shared creator_id would trip the rate limit.
SCENARIOS = [
    {
        "name": "c1 my writing",
        "criterion": 1,
        # Pass: at most 1 of 10 comes back guess "ai", in every trial.
        "texts": MY_WRITING_C1,
    },
    {
        "name": "c2 AI set",
        "criterion": 2,
        # Pass: mean confidence of this set minus mean of "c2 human set" >= 0.30,
        # in every trial.
        "texts": AI_UNEDITED,
    },
    {
        "name": "c2 human set",
        "criterion": 2,
        "texts": MY_WRITING_C2,
    },
    {
        "name": "c3 label coverage",
        "criterion": 3,
        # Pass: "human", "unsure" and "ai" each appear at least 2 times in the 15,
        # in every trial.
        "texts": MY_WRITING_C2 + AI_UNEDITED + AI_REWRITTEN_BY_ME,
    },
    # Criterion 4 (appeals) is tested by hand — run_eval.py only calls /submit.
    {
        "name": "c5 bad input",
        "criterion": 5,
        # Pass: every one returns 4xx (never 500) with an "error" field, and adds
        # one "event": "rejected" entry to GET /log, in every trial.
        "bodies": [
            {"creator_id": "eval_bad_missing"},                 # no text field
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   ", "creator_id": "eval_bad_spaces"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 42, "creator_id": "eval_bad_number"},
        ],
    },
]

def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
