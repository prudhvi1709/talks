# AI as Your Co-Developer - Transcript

**Host:** ...we are putting AI to use everywhere, literally everywhere. The code is written by AI, some people are generating their user stories by AI. What if we can put it to use in the workflows as well - of course the database will nicely relax and be like, "ah, I can't get it out." So, we have a really special person coming up for another special session, Schema Forge. Give a huge round of applause for Prudhvi.

**Speaker:** Thanks for this introduction. We've seen all the competition for your coding - Claude Code, Gemini CLI, Codex CLI, all day. What if we use AI as your co-developer, alongside you - not replacing you, but working with you, to accelerate your work? You'd have also seen a diagram earlier in the day showing there's no equilibrium between a developer's speed and accuracy generating code, and the pipelines - whatever those pipelines are - for production. So we came up with an idea: use AI, or an LLM, to generate those pipelines automatically, with you not having to do much for it. Let's dive in - I won't be using slides much, this will mostly be a live demo.

So, as we've discussed, AI helps with autocomplete, debugging, documentation, RAG over documents. What if it also helps design data pipelines? That work becomes faster. There are obviously value layers to consider, but the crux of this is having AI generate the schema, the documentation - the parts where a data analyst, or whoever's curating the data, spends a lot of time. You get a messy CSV, you clean it with pandas or whatever, and then you have to document every row, every column, what it's doing, every table, what it's doing - and that typically takes real time, on top of everything else you need to do. What if you just upload the dataset information and let it generate that for you?

Let me show the dataset first, then we'll go into the live demo. Here's the dataset - six tables, interconnected with each other, with any number of columns, each serving some purpose. But looking at it at first glance, I don't know what some of these columns are. Some are self-explanatory - patient ID, first name - but I don't know what "PT" is, what "FL" is, what "BM" is. This is very common with the datasets we deal with day to day - that's deliberate here too, since the intent of this synthetic dataset is to showcase exactly this problem, and how AI can help with it.

So let's put this into Schema Forge, to generate schemas, column descriptions, and dbt pipelines - dbt being the data build tool that helps you check the quality of your data, so it becomes a quality-checking layer too, alongside the ingestion part, where you convert from one source format to another. I'll upload the dataset now and see what happens.

Notice we're not passing any of the actual data - we believe these datasets often carry confidential information that shouldn't be shared with a third party. What we pass instead is the schema of the data: your column names, the type of each column - for example, "name" is a string. The schema itself is self-explanatory enough for an LLM to understand what the dataset is about.

So I upload it, and here's what it comes back with for the patients table - it's a dimension table, "patient demography and study participation information." It gives a basic description of the table, along with column-level schema descriptions and some flags - primary key, foreign key, and PII, personal identification information. From just the column names, the descriptions, and these flags, we get a solid basic understanding of what the dataset is about - all of this without doing much beyond passing the schema. For example, I mentioned I didn't know what "ETH" was - it says patient ethnicity flag, African American, European, and so on, following whatever categorisation the hospital uses; "BM score" is a numeric score, and it gives example values too. It also flags the PII fields we'd need to anonymise before doing anything further with the data.

All of this got built in about a minute. The schema-generation step itself would normally take a day or two to get to something reliable - I won't claim it's a hundred percent perfect, but call it ninety-five percent accurate (that number's illustrative, not measured), and you already have a very good starting picture of what your dataset needs. After schema generation, we pass that schema along to generate column-level descriptions and initial data-quality checks - and to do that, first we need the data understood, which is exactly what those descriptions give us. It creates constraints per column - for example, patient ID is an integer, not null - and it also cites the foreign keys it's inferred.

The reason we do this - to eliminate hallucination - is by asking it to cite what it's basing its answer on, to show how confident or grounded it is, so we know it isn't hallucinating about the data. It generates data-quality observations from the schema and gives initial constraints to check against. From this, you also get an ER diagram - visualising the dataset with its foreign-key relationships, one-to-many, many-to-many, and so on. Documenting a dataset like this normally takes real time on its own; the intent of an accelerator like this is to act like a co-developer, saving you that time so you can spend it elsewhere.

Once we have the diagram, there's a lot you can do from here. For example, under joins and models, it suggests joining the patients table in a particular way to analyse patient medication history, or joining lab results with patients to profile clinical lab values - recommendations that help you get a clearer understanding of the dataset, generated from what's already available. With that scaffolding ready, we generate the dbt rules that check the quality of the data. Why check quality at all? Obviously we clean data before using it for training or anything else, but we also need to know how good the data actually is. dbt is a Python-based rule framework where we can generate rules and test them directly against the dataset, using the context we've already built. It's still generating as we speak - meanwhile, happy to take questions if anyone has any.

## Q&A

**Audience:** The Excel you uploaded is a single file - is any foreign key actually defined in it?

**Speaker:** No foreign key is defined, nothing is defined - it's just data across six tables, six different sheets, with no relationships specified anywhere.

**Audience:** So how does it identify anything, then?

**Speaker:** It identifies the primary and foreign keys on its own - it was able to relate the dataset from one table to another. These sheets were originally generated from a database that did have real relationships - this is synthetic data, generated intentionally so every test case we wanted to check would hold, for example that every table connects somehow, one-to-one or many-to-one. Whatever relationships it infers do match the original relationships, at least for the data I used.

**Audience:** Where do you tell it that this is the original relationship - do you give it that instruction somewhere?

**Speaker:** We don't say anything about the relationships at all. We just send the schema - not the data, just the schema. While processing the schema, it understands the IDs and their data types, and from that it infers what the relationships are. We don't state them explicitly - we could, but that's up to you. It doesn't even need to rely on the column names to do this.

**Audience:** How is it doing that, exactly - you upload the Excel and it just figures it out?

**Speaker:** The intent of this demo isn't for you to use Schema Forge exactly as shown - the point is that you can use AI as a co-developer to accelerate your own workflow. You could just as easily send it your headers and get the schema out of that, whatever's useful for your case - the core idea is having AI accelerate your process. This is just one example I built; depending on your case, you could upload your own data directly and get a similar result.

**Audience:** So you're not sending the actual data anywhere?

**Speaker:** Correct - you have complete privacy over your data, since only the schema goes out, never the data itself.

We generated the rules - let's look at what it produced for the patients table. For clinical study ID, it says it's a study identifier and creates a test that it should never be empty, with the relationship pointing to the adverse-events table as a foreign key. Patient sex may be male, female, or other. Ethnicity flag has its own constraint. Score should be greater than or equal to 45 and less than 66, and so on. With that, you get an initial quality analysis of your data within five or six minutes - you can run it against your data and see which test cases pass or fail, then fix the data before it goes to production. This works well as an initial pass on your data, and there's also a human-in-the-loop chat option to add or change rules as needed.

So the crux is: you can build all of this in a single shot, with AI as your accelerator. And from building this, I picked up a few lessons I'd like to share.

The trade-off is speed versus correctness. AI can generate code very fast, but when you validate it against what an expert would have written, the correctness might or might not hold up - so you need rigorous tests and clear instructions for whatever you're using. On hallucination: the typical failure is when it's working with your data and just guesses. The way to handle it is to ask it to cite what it's referring to, ask it why it's referring to that - and, as was mentioned earlier in the day, using an LLM as a judge is also a good option, though structuring your input well is really what reduces hallucination in the first place.

On reliability: I found that defining the tests before generating the code works really well - for example, saying "I need to test this feature by feeding it this dataset, and I want the code here to make that test pass" gives it complete context to generate against, and it does a good job with that kind of framing, from what I've seen. And obviously, having a human in the loop increases the reliability of what actually goes to production - so the pattern becomes: use AI, review the results as a human in the loop, then ship to production.

The key takeaway is that AI as an accelerator can help you build production-ready code - at least here, dbt rules and the surrounding code. I should also mention the ingestion side, which I forgot earlier - ingestion is one of the areas where you'd otherwise sit and write the code to transform data from one format to another. But since we already have the schema, we can use that to generate whatever ETL code is needed - extract, transform, load - as Python scripts that convert your dataset from one format to another. For example, I selected a SQL database as source and a Parquet file as destination, hit generate, and it produces the conversion script - you just run it locally, no extra work needed to get your data transformed.

So AI can help accelerate your speed a lot, as others have said through the day too - and I agree with that. But human review and testing are what actually let you push it safely into deployment and production. That's pretty much it from my side - happy to take questions.

**Host:** Any questions?

**Audience:** Is there a way to expose this entire thing as an API?

**Speaker:** Could be - this is currently in JavaScript, but we could wrap it as an endpoint that does the same thing.

**Audience:** For each patient there'll be a separate persona - how do you handle that changing in real time?

**Speaker:** It doesn't take your data at all, only the schema - so even if a value like a phone number changes, or matches some regular expression pattern, it only ever considers the schema, not the underlying data, so changes to the data itself don't affect it.

**Audience:** Any specific reason you picked dbt as the framework?

**Speaker:** I was exploring how to check data quality using LLM-defined rules, and it did a pretty good job generating dbt rules specifically - no deeper reason than that; the exploration led me there. You could use other rule frameworks by guiding or instructing it differently, but I found dbt rules were accurate for what I needed.

**Audience:** Would you be able to run this locally, to check quality without sending anything out?

**Speaker:** Not currently in this exact form - the dbt scripts themselves are just plain files, so they can be packaged into a model and run against your dataset entirely on your local system, without sending anything to a server. So you'd have full privacy and control.

Any other questions - I'm happy to be reached afterwards too, and open to related projects, so feel free to get in touch.

**Host:** Did you all enjoy the session? Awesome - let's have a round of applause.
