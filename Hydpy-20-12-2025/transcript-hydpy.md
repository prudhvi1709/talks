0:01 Hey, hi all. Uh this is Prudi. I work as
0:05 a data scientist at Graminar uh a data
0:07 science company. Uh I usually worked
0:11 with LLMs means I try to incorporate
0:15 LLMs wherever it is needed or wherever
0:17 it's not needed then I'll realize okay
0:19 this is not needed here and wanted to
0:21 share some experiences with you guys
0:23 such that you can incorporate all the
0:25 LLMs that you use. I believe all of you
0:28 are using LLM's daily daily basis right
0:31 so wanted to share some experiences as
0:33 that you can also use LLMs in your daily
0:36 life which will make your life easier so
0:39 it's not replacing humans but they are
0:41 with you along with you to fasten your
0:44 process so you can do your job in one
0:47 day instead of 3 days right so I'll come
0:50 to the point why we need LLMs in data
0:52 engineering now I am focusing on one
0:54 particular topic here which is data
0:56 engineering ing because somewhere uh in
0:59 the working days I felt that the the
1:01 engineering team is being doing the data
1:03 pipelines, ETL pipelines, injection
1:05 pipelines or quality pipelines you know
1:08 we can actually automate this and we can
1:10 actually accelerate this uh before
1:12 without doing it manually every time.
1:14 Right? So we see that you know modern
1:18 data systems are large and constantly
1:21 evolving. We see that models are being
1:23 released very frequently. We see that
1:25 models are very fast and accurate and
1:28 why don't we use that in our enterprise
1:31 level itself right with some guardrails
1:34 what we have to introduce but we'll see
1:37 that so if you come to data engineering
1:41 pipeline uh so there will be a lot of
1:43 pipelines right the quality pipelines
1:45 injection pipelines the ETL pipelines
1:48 which is extract transform and load
1:50 where you'll transform a database to one
1:53 to other which usually takes a lot of
1:56 time and usually have to maintain a bit.
1:59 Now if something is break in between or
2:01 something is broke in between if there
2:03 is a change in schema or if there is a
2:05 change in the data if a value becomes
2:07 nullable because the data keeps updating
2:09 keeps updating it's not constant. So if
2:12 a value becomes nullable the pipelines
2:14 which were already built will not broke
2:16 instantly. It will break break after a
2:19 time or after a particular time period.
2:22 Now when it breaks we have to come
2:23 debugging debugging debugging and then
2:26 okay later we realize that this where it
2:28 broke. Instead what we can do we can
2:31 automate few things on pipeline itself
2:34 where we can reduce the manual effort
2:37 and we can you know
2:42 we can uh actually automate and
2:44 accelerate the things we do. So usually
2:47 in data engineering uh in building the
2:49 pipelines the human which is us the
2:52 employees spend times for writing
2:54 schemas. Schemas are basically the data
2:57 types of your data set. So you have a
2:59 data set you have a SQL database you
3:00 have have a DB or whatever it is. We'll
3:03 write a schema for it. Schema tells what
3:06 column type is what of type and which
3:08 data type it is. So we write schemas we
3:11 write dbt tests. DBT is a data build
3:14 tool. It's a Python framework where it
3:16 used to check the quality of your data.
3:19 So instead of you being a data analyst
3:21 going through each and every row, we
3:23 write some rules and we'll test it on
3:25 the database. So we we'll get an idea
3:27 how quality of our data is and how good
3:29 are we maintaining it and debugging
3:31 mismatches obviously we'll they spend
3:34 more time on. Now we have LLMs who are
3:38 good at reasoning, good at understanding
3:40 context. We don't want LLMs to come in
3:44 our pipelines and guess something what's
3:46 happening. Instead, uh Sanjit was saying
3:49 that building context is more important.
3:51 So we'll build context for that and then
3:53 we'll use in our pipelines. So because
3:55 they are good at reasoning, because they
3:57 are good at understanding the context,
3:59 we'll leverage that use to our
4:01 pipelines.
4:03 So when I say schemas, schemas are
4:06 actually living artifacts, right? uh
4:07 they are not static contracts that you
4:09 write once and then you leave it and you
4:12 ingest in the pipeline they are actually
4:14 change they change according to the data
4:16 changes so your data keeps updating your
4:18 keep your data is life and then your
4:20 schema is also will keep updating
4:23 so for building the context for an LLM
4:26 you don't need to give the database
4:27 itself to an LLM you don't need to pull
4:30 all your uh database to an uh chart GPT
4:33 or cloud models to understand what
4:36 exactly is happening instead Instead we
4:38 can give schema of the data set to an
4:40 LLM. So schema comes with the column
4:45 names row rows and the data types of the
4:48 columns. If you provide that context to
4:50 the LLM which which L it is your choice
4:53 open a anthropic whatever it is and then
4:55 we say okay do this this it will have a
4:57 better context and an accurate results
4:59 we can do that. So I'll show something a
5:02 live demo here where I build something
5:05 that I felt is an accelerator and which
5:08 is an accelerator. So it's called schema
5:10 forge where I actually send the schema
5:12 of a data set that we upload to an LM
5:15 and ask it to build three things. One
5:18 the description of the data sets each
5:20 and every row what it's doing each and
5:21 every table what it's doing and two the
5:24 relationships and entity diagrams. So
5:26 usually the engineering team also spends
5:28 in creating the entity diagram uh and
5:31 the joints and relationships modelings
5:33 modelings and all and three at last with
5:36 all this context I ask you to generate
5:38 dbt rules with which I can check the
5:41 quality of the data that I have. So yes
5:45 so it's a web based currently that I
5:47 built but we can have this as APIs and
5:50 whatever in the enterprise level code
5:52 system has when we can adapt to it. So
5:54 I'll uh the data flow is like this.
5:57 We'll take the data. We'll infer the the
6:00 we will pass it to the schema forge and
6:02 what it does is it infers the schema. It
6:05 detects the relationships and modelings.
6:06 It detects the data types and then it
6:09 generates the DBT rules and we'll
6:10 validate accordingly. Right? I'll jump
6:13 into the live demo. Uh,
6:17 just
6:24 let me pull this.
6:38 So before uh showing the demo itself,
6:41 I'll show you the data base or data set
6:43 that I've been using so as that you'll
6:45 get a better context of what's been
6:47 happening. Right? So this is a database.
6:50 I converted it to Excel such that I can
6:52 show it clear.
6:54 Okay.
6:58 Is that clear?
7:01 Okay. I can't see it.
7:03 So yeah, this is the data data set I'll
7:06 use to show the live demo. Uh so this is
7:10 how it is. It has six tables. Consider
7:12 each sheet in the Excel as each table.
7:15 It has multiple this is a pharma trials
7:17 data set where I created. Uh so it has
7:20 patients data, it has doctor's data, it
7:23 has lab results, it has adverse events
7:26 with the related to the pharma trials.
7:28 Right? So this data has a lot and lot of
7:31 information with it. Now by looking at
7:35 the data as a third person which who not
7:38 built the data I don't know what pt type
7:42 is and this is how typically the data
7:43 sets be or the data basis be because
7:47 someone develops someone organizes it
7:49 they have the documentation but as a
7:51 third person who looking at it without
7:53 any context I don't know what pt type is
7:55 I don't know what eth is I don't know
7:58 what bam score is right so and even llm
8:02 doesn't know it because we haven't
8:03 passed it yet. So what we will be doing
8:05 here, I'll just up and this has six
8:07 tables. You can see six sheets. I'll
8:08 just open them. Uh which is of very
8:12 similar types, right? So what I'll do
8:15 now is upload this to schema forge and
8:18 let's see what it does.
8:29 So I'll upload this. Uh, you need to
8:30 configure the LLM, which I did.
8:35 Okay,
8:36 apparently I didn't.
8:39 Okay, I'll just let me one second.
8:46 I'll just pass my key and give it. It's
8:48 a secret.
9:13 Yes. Uh
9:16 again,
9:20 so yes, I configured OpenAI. uh here in
9:23 in this case I'm using GPT 4.1 mini
9:25 which is kind of outdated but I'm fine
9:27 with it. Uh so what it does the
9:31 immediate I upload it generates it's
9:33 take the schema of the data set along
9:35 with some sample rows that I sent
9:37 because I want the LLM to be most
9:39 accurate as possible because I don't
9:40 have any uh personal information or
9:43 client information in this particular
9:44 data set. So I pass 10 random rows not
9:47 the head of the data set but 10 random
9:49 rows of each sheet along with the schema
9:51 of the data set to give the LLM better
9:53 context. So as good the context is as
9:56 good are the results are. So the
9:58 patients table which we saw. So it
10:01 detected PT type is a string and it says
10:03 patient type code. It's a category ABC
10:06 which may hospital have or may hospital
10:08 have categorized and and the ETH score
10:11 is a string as well and it says
10:13 ethnicity flag. So maybe it's an
10:15 international hospital and they have
10:17 African, Asian and Latin American all of
10:20 those.
10:22 So and it does same for all the tables
10:25 that it have. I haven't showed you the
10:26 six tables but these are the six table.
10:28 The benefit here is by giving the schema
10:32 and sample rows of each table in the
10:35 whole database. It also recognized the
10:37 relationships and the modelings of the
10:40 data set. So what is the primary key of
10:42 this table? For example, you can see the
10:43 patient ID is primary key along with the
10:46 PII tag. So PI is personal
10:49 identification information where it
10:51 treated as sensitive and it will not be
10:53 shown everywhere. So it detects the
10:55 foreign keys, it detects the primary
10:56 keys and it detects the PIIs. Now I have
11:00 very good understanding very good uh you
11:02 know information about the data set as I
11:04 have right. So it generated all the
11:07 schema for each table in the database
11:10 and it also gives the constraints of
11:12 each columns. For example, for example,
11:16 in patients table in the patient ID, the
11:18 basic constraints it needs to have it
11:20 should be unique because each patient ID
11:23 is mapped to each patient and it should
11:25 be not null obviously and it should be a
11:27 positive integer. So it's a foreign key
11:31 references. It says clinicians site ID
11:33 which is a clinician's table. uh it
11:35 connected to a clinician's table with a
11:37 site ID as a foreign key and it detects
11:40 a lot and lot of patterns in between the
11:42 database. Now as I have this why don't I
11:46 create the diagrams and relationships.
11:49 So usually the engineering team will sit
11:52 and understands the data and uh you know
11:56 have the uh diagrams ready but in one
11:59 shot I have the diagrams
12:01 I just because the LLM understood what
12:04 the relationship between the tables each
12:06 and there and it detects the foreign
12:07 keys and it detect the primary keys. It
12:09 was able to join all the tables that I
12:11 have which is accurate that I can say
12:14 and it also detects the relationships.
12:16 So let's say prescriptions tables and
12:18 patients table. It says join these
12:21 tables with inner join for this
12:23 particular use case. So it's giving me
12:25 the along the additional information
12:26 that I can implement on our databases
12:28 that I can draw more information and
12:30 draw more insights. This how it now
12:33 we'll come to the part where we'll check
12:35 the quality of the data and we'll also
12:38 come to the part of injection. Now I'll
12:40 generate the dbt rules which is data
12:42 build tool. As I said it's a Python
12:44 framework to you know test the quality
12:46 of the data. Now while generating it has
12:49 the context of schema and whatever the
12:51 relationships are and it generates three
12:53 things. The SQL which is an actual code
12:57 to apply on our data set without we
12:59 doing nothing much and the AML explains
13:01 what and all it test it's being doing
13:03 and the tests which are map put to SQL
13:06 and the ML. So now I have the SQL which
13:10 I can directly run. Now I have the AML
13:12 to understand what and all test has been
13:13 happening and now I have also everything
13:16 ready. It's been generating but
13:20 let it generate. It might take some time
13:21 but yes so
13:24 we have ER diagrams ready. We have
13:26 joints and modelings ready. We have DBD
13:28 rules ready. We'll also have the
13:30 injection ready. Injection is nothing
13:32 but ETL. Right? So let it generate. I'll
13:36 wait for it generate generation. I'll
13:39 show data injection meanwhile. So what
13:41 injection is uh we have our data bases
13:45 in particular format. For example, I
13:47 prefer SQLite database. They prefer
13:49 posts or that format. They prefer duct
13:52 DB which is uh anything. So they prefer
13:54 something. Now injection comes where we
13:57 can convert one database to another
13:59 database. This can be do in two ways.
14:01 One is ETL and one another is ELT. ETL
14:05 is where we use Python which is a nonsql
14:08 language to convert from one database
14:10 format to other. I what I'll do here is
14:12 I'll select a source format which is for
14:15 example here is SQL database and I'll
14:18 select a parket file and I'll say
14:21 generate and if you have any concern for
14:24 example I don't want PII information
14:26 which are being tagged for example
14:28 patient name I don't want patient name
14:29 row to be existed in the converted file
14:32 I can just say it and you can have it in
14:33 the ready so it generates the Python
14:36 scripts to convert from one another
14:38 which are actually working I tested
14:40 every of them locally
14:41 So they'll work seamlessly. So we have
14:44 schema ready, we have relationships
14:46 ready, we have air diagram ready, we
14:48 have db rules ready, we have injection
14:51 scripts ready. This reduces almost 80%
14:54 of pipeline timing or to build a
14:57 pipeline for an engineering team to
14:59 build in a month or so. So for every
15:02 project we build a context, we'll pass
15:05 on what and all we need, we'll let LLM
15:07 have us generate code. LLMs are very
15:10 good at generating code but not
15:11 guessing. So we'll leverage that uh you
15:14 know advantage to generate the code to
15:17 whatever we want and then use it in our
15:19 pipelines which will accelerate our work
15:22 which we can also finish faster. So this
15:26 is what and I believe by this time it
15:29 should be generating the DBT rules. Yes,
15:31 it is generated. So for example for
15:34 patients table and the test it's been
15:36 doing is the patient ID it's visible
15:39 right let me just zoom in
15:44 so the patient ID should be an unique
15:46 identifier for each patient in the data
15:47 set and it should not be null it should
15:49 not be unique which are the constraints
15:50 we seen in the column descriptions and
15:53 it says patient ID greater than zero and
15:56 and if you go to date of birth it should
15:58 be this particular regular expression
16:00 which is of 224 format or 422 format in
16:04 this case which is y
16:07 mm and dd format and yes so it goes
16:11 through every column it go it creates
16:13 tests for every column which will help
16:15 us to check the quality of the data hold
16:17 the I mean we have quality for every row
16:20 right we have nullables in each row we
16:23 have we will be having nullables we will
16:24 be having some miscorrected information
16:26 so we can detect with it and and we can
16:30 leverage how the embeddings which Sanjit
16:33 said by just creating a chatbot on top
16:36 of it. So once we have all the
16:37 information we'll convert all these two
16:39 embeddings and we can use a chatbot on
16:42 top of it. For example, I'll ask it to
16:44 add an new rule. It does add a new rule
16:46 by understanding what the context is
16:48 already been generated. So it's kind of
16:51 human in the loop. We are using AI to or
16:54 in this case LLMs to accelerate our
16:57 process, accelerate our pipelines and we
16:59 have everything ready in 2 minutes.
17:03 So that's how we can leverage and this
17:06 is only I'm just uh presenting for an
17:09 engineering use case but you can use it
17:11 for data scientist use case where he
17:13 will find the hidden patterns he'll
17:16 visualize the data or whatever it is. So
17:19 the crux is we can use LLMs by giving
17:22 providing by providing the good context
17:24 to have it whatever we can do let it let
17:27 it do so it's not replacing the humans
17:29 we are the humans are using LLM as a
17:31 second brain right and we can accelerate
17:33 things quite faster I I I need to do
17:36 this in 10 days or I did it in 2 minutes
17:39 there will be human in the loops there
17:41 will be guardrails and there will be a
17:42 lot of things to check this but the we
17:45 have the you know the initial
17:48 scaffolding ready so we can be fast in
17:50 our processes for the next pipelines. So
17:54 yes, that is pretty much from the live
17:56 demo. I'll switch to the PPT. I should
17:59 have it somewhere.
18:00 Yes.
18:04 Yeah. So that's the data flow. We
18:06 uploaded the data set. We retrieved the
18:08 schema. We identified the information
18:10 and we created the visualizations and
18:12 rules what whatever you want. and yeah
18:16 zero to DBT rules in 2 minutes and it
18:20 detects the PI as well because it has
18:22 the information of what and all rules we
18:23 have and what and all data types we have
18:26 and as I showed the chatbot I haven't
18:28 showed its working version but it's a
18:30 natural language to SQL chatbot where
18:32 we'll ask a question of generate a new
18:34 rule it does generate the SQL code for
18:36 it so we and we can run it everywhere
18:41 right it's not a product page but we can
18:43 run it in the browser You can run it in
18:45 your back end. You can integrate with
18:47 your CI/CD pipelines and we can you know
18:52 everything is deterministic and
18:53 reviewable here. So you can edit
18:56 everything and it is everything is
18:57 visible to you. So it's a pretty good
18:59 way of uh accelerating things that you
19:02 actually do in the daily life. And by
19:05 doing this what actually stays the same.
19:07 ETL is owned by Python which we also
19:10 traditionally use. So we can have the
19:12 Python pipelines ready here and DBT owns
19:15 the execution. So for example, schema
19:18 force generates the rules and DBT runs
19:20 them. So if you download them locally,
19:22 you install the Python package, install
19:24 DBT, it will take care and you will run
19:27 the DBT rules that are being generated.
19:29 So it's a tool that we not think as a
19:32 replacement of a human because everyone
19:33 is afraid of okay AI is taking my job
19:35 but it's not. So we are accelerating our
19:38 job with AI. So it's kind of a second
19:40 brain that we use.
19:42 With that I wanted to conclude and yes
19:46 you can try it's a open source full
19:47 whole codebase it's there and you can
19:49 connect and I can also be in an open
19:51 source projects if anyone wanted a
19:53 collaboration you can scan the QR for
19:55 GitHub and LinkedIn all of them and I'll
19:58 take the questions now if Ready?
