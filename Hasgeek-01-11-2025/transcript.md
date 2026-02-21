5:01:57
this I had a question for you that um we are putting AI to use everywhere
5:02:03
literally everywhere. The code is written by AI and you know some people are uh generating their user stories and
5:02:09
all by AI. What if we can put it to use
5:02:16
in the workflows as well much easier right of course the database
5:02:21
will nicely relax and be like ah I can't get it out. So yeah we have a really
5:02:26
special person coming up uh for another special session schema forge. Give a huge round of applause for Prudi.
5:02:36
Thanks for this introduction. So yes, uh we've seen all the
5:02:42
competitions for your coding cloud code, Gemini CLI, Codex CLI all the day. What if we use AI
5:02:51
as your code along with you? So not replacing by but along with you. So how
5:02:57
much you can accelerate your work and you also seen an diagram shown first talk uh saying that there is no
5:03:04
equilibrium where developer has its own speed and accuracy of the generating code but not the pipelines for
5:03:12
whatever the pipelines are pipelines or production. So we came up with an idea where we can use AI or LM to precise uh
5:03:20
to have it generate the pipelines automatically without you doing you not
5:03:26
doing much for that. So let's dive in. Uh I'm not I'll not be using slides. I
5:03:33
mean not using live demo most of the time. So yes. So now as we spoke uh AI
5:03:42
helps you in auto completions. helps you in debugging, helps you in documentations, helps you in rag for
5:03:50
document or not. What if you also design data pipelines, what if you also
5:03:55
designation pipelines, right? So, it's it will be the work will be faster.
5:04:01
Obviously we have some value layers but the crux and theme of is to have AI to
5:04:08
be generating the schema documentation some so typically a data
5:04:13
analyst or someone curating the data we'll spend a lot a lot of time for
5:04:19
documenting etc. So you'll have a messy CSV you'll be cleaning that using pandas
5:04:24
whatever it is and you'll be documenting every row and column what it's doing every table what it's doing and
5:04:31
typically it takes time and often doing that you also need to do any number of things to be pass
5:04:39
what if you directly upload provide the information of the data set to an
5:04:45
generate whatever it can let's see that uh I'll be I'll be using the data set
5:04:51
here. I'll show the data set first and then we'll dive into the live demo. So
5:04:56
here is the data set I think it's buried there but the QR code I initially has that I want
5:05:05
I can show that I can but this has six tables six tables interconnected with each
5:05:11
other with n number of columns saying whatever the purpose and serving whatever purpose
5:05:17
right but looking at the data set on the first view I don't know what some of the columns are some of the columns are
5:05:24
self-explanatory for example patient ID self-explanatory study
5:05:29
first name is but I don't know some of the columns what is PT I don't know what
5:05:35
is FL I don't know BM I don't know and
5:05:40
this is very common where we have the data sets right here I call B2 data set
5:05:46
this is very typical behavior how the data set will be database so so this is
5:05:52
the behavior of the data set is the intention of creating a data set itself to show the showcase I mean showcase the
5:05:58
leverage of AI we can take that so let's I'll just put this data set into schema forge uh to generate schemas generate
5:06:07
column descriptions generate DVD pipelines uh what DVD pipelines are data
5:06:13
build tool where it helps you to check the quality of your data so it becomes a
5:06:19
quality setting also along with the injestation parts injection where you convert one source format to another
5:06:26
database format right I'll be uploading this data set so let's see what happens
5:06:37
so what it takes we are not passing any of the data from the data set because we
5:06:43
believe the data sets we have confidential information they not are not preferable to share with thems
5:06:50
What we doing here instead of passing the data we are passing the schema of the data schema of the data will have
5:06:56
your column names will have your uh type of your columns. For example,
5:07:02
name is a string right and the the schema itself is selfexplanatory for an
5:07:08
LLM to understand what our data set is. So I upload the data set and see what it has uh with the patient table. It's a
5:07:16
dimension table. It says patient demography and study participation information. So it gives basic data
5:07:22
basic uh description about the data or the table that we have for the patient table along with the column with the
5:07:29
schemas description and some flags. Now what flags can help right we have primary PK is primary key FK is foreign
5:07:36
key and PI is personal identification information. What we can do with this? We have our
5:07:42
column names. We have our descriptions of the row and we have our flags. From this we can have I mean we can
5:07:49
understand the basic following of the data set how what the data set is about basically. So we have all the tables and
5:07:56
the descriptions defined here without much doing anything except passing the schema of the data. Right? So we have
5:08:02
our for example I mentioned any type I don't know. So it says patient type of classification ABC which may be followed
5:08:10
by any hospital is ethnicity flag African American
5:08:15
European blah blah blah and BM score is numeric score I guess it is CP I mean
5:08:21
it's also giving the examples that so yes and it also flags the personal identification information which we need
5:08:28
to anonymize before doing anything right so this is how
5:08:34
it built in couple of minutes I would say 1 minute the schema generation
5:08:39
itself take a day or two to have a very good I mean I don't say this 100%
5:08:44
perfect but 95% accurate the number is made up but I mean I have a numerical uh
5:08:49
tag for this but we have a very good information about what our data set needs so after the schema generation
5:08:57
we'll pass the schema to have each column descriptions where we'll be doing initial quality observations so then
5:09:04
more of So what we're doing here is to check the quality of the data and how are we checking the quality of the data
5:09:10
is by generating some rules. I'll be going to that in short while. But to have all those things first we need to
5:09:16
understand the data. To understand the data we are basically descriptions of each column what it's doing. This is
5:09:22
what I want. So it creates some constraints that for every column for example patient ID is an integer where
5:09:28
the constraints are not and it also sites the foreign keys. What
5:09:34
we observe is to eliminate the hallucination of from the we can ask the
5:09:40
citations from the itself to show how confident it is or how accurate it is
5:09:45
such that we can know it's not hallucinating about the particular problem or in fact particular data right
5:09:51
so it it also creates the data quality observations from the schema and gives
5:09:58
some constraints to check the first initial from this you'll be able you
5:10:03
will get the ER diagram. ER diagram is where you will visually uh you know
5:10:10
visualize the data set with foreign keys relationships and what relationship it is what to relationship many
5:10:16
relationships and blah. So what generally diagram also takes I mean
5:10:21
documenting the data set itself takes a lot of time. The intention of these type
5:10:27
of accelerators is to have it as a co-developer. So I said it saves a lot
5:10:32
of time for you to put some other things which are being done by AI right now. So
5:10:38
we have diagram set. So basically the documentation of the data is we can do a
5:10:44
number of things from here. So for example if I go to joins and models it says joins patient table with the
5:10:50
descriptions to analyze patient medication history. So what it says is join this table by this particular
5:10:56
pattern of this C state and it will be able to analyze the patient medication
5:11:02
and by joining the lab results with the patients to profile clinical lab I mean to to profile the clinical lab values
5:11:09
you join these these tables. So we have all the recommendations from the available right now which is few
5:11:16
recommendations came to help to analyze the data set to get a very good clear
5:11:22
understanding of the data. Now as we have our all scaffolding ready we will be generating the dity rules which helps
5:11:29
us to check the quality of the data right now what why we need to check the
5:11:35
quality of the data. Obviously we need to do do the data cleaning before one and all we do but we we need to train
5:11:40
the data whatever it is we need to do the data cleaning for that but we also need to check how quality the data is
5:11:47
for that we dbd is a python based rule
5:11:54
classifier where we could generate the rules test it directly on the data sets using the so as we have the information
5:12:02
all about the data that we have we can we I generated the rules so and it gives
5:12:08
the rules it's still separating but once we have the rules we can take the rules and directly apply on our data set to
5:12:15
check how good the data is or how good our data set is and it also gives which
5:12:21
test cases pass which test case such that we can directly site to that and
5:12:26
you know rectify the data that we have so it's still generating meanwhile if you have any questions till now I'll
5:12:33
take it Excel that you uploaded is a single column.
5:12:38
Single no foreign key is defined in that. No, no foreign key is defined. Nothing
5:12:44
is defined. It's just data with six tables. You give six different tables.
5:12:49
Six different tables which is six different sheets. Six different sheets and there is no relationship defined or anything. No,
5:12:56
it identify what? Yes. So it identifies the primary keys and foreign keys along with the primary keys and foreign keys. We were able to
5:13:03
go data set from one and the tables from another. But these Excel sheets were
5:13:10
generated from certain existing database which had a relationship or kind of we this is synthetic data. Uh we
5:13:18
intentionally had it uh we generated the data uh to have for every test case that
5:13:23
we want to test uh to be fine. For example, each table needs to be connected somehow
5:13:29
either one to one or 9 to one. But but this whatever you're trying to
5:13:35
create the relationships the original relationships do or they these are
5:13:41
they do match at least for the data I use they do match and where do you tell that it has to match like you give that instruction
5:13:47
somewhere that this is the original relationships and this is what we we don't say anything about relationship at all. We just send the
5:13:53
data along with the schema. I mean don't send the data but send the schema of the machine. So while sending the schema it
5:13:59
understands the ids and their data type it it gets to know what relationships
5:14:05
that have and how it is. We don't say anything about the relationship.
5:14:10
We could say, but that's up to you. It doesn't even pick up from the column name something like that
5:14:18
key f no
5:14:29
we can. But how are you doing it? You'll be uploading your Excel sheet and
5:14:35
it's like only the
5:14:40
you could feel. So the intention of showing this demo is not to use schema course directly in your I'm saying that
5:14:46
you can use K as your code developer to accelerate your so you could use that for that you can also send the headers
5:14:53
to get the schema and whatever it is doing for you the crux of it is to have
5:14:58
your AI as your uh code to accelerate your so this is just one of the product
5:15:05
deities that I made but yes I mean depending on you you will be you can
5:15:10
upload your data directly try to charge it and get a better.
5:15:18
Yes, that's fine. But here you are sending those to those you just send. So you have complete privacy of your data
5:15:23
what you have. So we generated a table to use for
5:15:28
example for the patients table let's see what and all it's taking. Uh
5:15:35
so clinical study study ID is clinical study identifier and the test it's creating is is should not be done and
5:15:42
the relationship basically is referring to the adverse events table is a field of study and yes so patient
5:15:50
sex may be male female or others right ethnicity flag should not be score is
5:15:56
some some should be greater than or equal to 45 and less than 66 and some
5:16:02
constraints right So with that you will be able to get the initial quality analysis of your data within just 5
5:16:09
minutes 6 minutes you'll be able to run this on your data and get whatever test
5:16:14
case pass failed and you can uh you know
5:16:19
rectify your data to pass it in the production. So this is this can be used
5:16:25
initially for your data feeding and whatever it is and also we'll have human
5:16:30
the loops chart options to add rules or change rules or whatever it is.
5:16:38
So, so the crux is you'll be able to create all of this in signal shot with
5:16:43
AI as your accelerator, right? And from all while building this, I've learned a
5:16:49
few lessons which I would like to share. Uh,
5:16:54
yes. So, the trade-off is AI can
5:16:59
the speed is correctness. AI can generate code very fast, right? But when
5:17:05
you validate it with the original code that you made which can be an expert code the correctness might or might not
5:17:12
be good right. So having you know how do you handle it by rigorous tests by clear
5:17:19
information by clear instructions to the you going to use and the hallucination
5:17:24
where structure hallucination is what a typical will give when you load it with
5:17:32
the data or whatever it is. How do you handle the definitions in any case? Ask
5:17:37
it to site the data it's referring to. Ask it to answer why it is referring to. Also, as you mentioned, LM as judge
5:17:44
would be a very good option to not for the hallucination but to the so
5:17:50
structuring the input that you are giving to the LLM would help in reducing the hallucinations from. Yes. So and how
5:17:59
the reliability of the errors right I found that the code it's generating by
5:18:06
defining your tests previously before it's generating the code is very good for example you need
5:18:13
to test this uh I say I need to test X feature by inputting this data set I
5:18:20
want to write the code here to have this test pass right so you are giving
5:18:26
complete context to generate the code for itself. It it does a very good job that's from my experience that I observe
5:18:33
and obviously having the human in the loop will increase the reliability that you can pass into the production. So the
5:18:39
integration pattern would be you use AI you see the results from the AI you
5:18:44
validate that as a human in the loop and then you pass it to the production. So deploy it into the production and pass
5:18:50
it to the production. And yes, the key takeaway is having AI as your
5:18:57
accelerators can help you build production ready codes at least here DB
5:19:03
rules and codes. I forgot actually I need to mention about the injection that
5:19:09
it has. So injection is one of the main problem or main body where we have to
5:19:17
sit and write the indestation codes while transforming a data from one format to another format. But we have
5:19:23
the schemas of the data set of initi. Now what can do is take the schemas to
5:19:29
convert whatever source file and format file is to generate whatever the ETL codes we have. Right? We have ETL here
5:19:37
which is extract platform load which helps you generate Python scripts which
5:19:42
will transform your data set from one format to other. So for example I
5:19:48
selected SQL database bucket file and I'll generate the scripts. It will generate a conversion script from your
5:19:54
source format or destination format without you doing anything much. We just
5:20:00
need to run the scripts in your local the data being transformed from on format.
5:20:05
So AI can help you a lot in accelerating your speed as I from everyone from this
5:20:14
area but I do also agree with that. So also human in the loop and testing it
5:20:20
will also help us to push it to the deployment and productions. So that's pretty much from my set and uh
5:20:28
I would like to have questions and happy to take them.
5:20:34
So guys, any questions? Anyone?
5:20:44
Is there a way that we can call this entire thing as an API? Could be. Uh this is currently in
5:20:50
JavaScript. We could have one end point that does all of this in that can do that
5:21:03
for each patient there will be a separate persona there right so how do
5:21:08
you like in real time keeps on changing so
5:21:18
why do you want to face personas here Uh yeah because each person have different
5:21:29
it doesn't take your data right it takes only the schema so for example the patient phone number is a plus one and
5:21:39
10 is regular expression what are
5:21:46
yes but that is the reason we are not sending any data to the we are just sending the
5:21:52
schema of the data set. We are not sending the data of the element. So even if it changes it considers only the
5:21:58
schema of the data
5:22:06
any specific reason for this entire thing.
5:22:15
Is there any specific reason you pick DBT as the label?
5:22:21
Uh I was exploring how to check the quality of the data from LLMs to be
5:22:26
defined in the rules. I found it pretty much did a very good job in generating DB rules. So no specific reason but
5:22:34
exploration made me to use D. You can use different rules by guarding or instructing everything but I found that
5:22:41
DB rules are pretty accurate from what it is. Would
5:22:49
you be able to do this without you be able to do it without
5:22:55
uh to run this locally and check your quality? Uh currently no I mean the
5:23:00
script itself or DP scripts the simple statements and files. So it will be
5:23:05
compacted into one model and will be running on your data set in your local system without sending anything to the
5:23:10
server. So you have your privacy, you have your uh complete ability to
5:23:22
any other questions I have my here and I'm open to any related projects as
5:23:29
well. So please feel free to contact
5:23:36
any questions there. Uh any questions? I think.
5:23:43
So, do you like the session? Awesome. Right. So, can we have a round
