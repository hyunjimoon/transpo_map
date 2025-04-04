# project instruction 
# Demand Modeling Recitation Planning Project

## Project Overview
This project prompt guides the weekly planning of demand modeling recitations at MIT, focusing on four key tasks that bridge instructor knowledge (Moshe) with student learning (via Angie's teaching). The structure enables efficient knowledge transfer through targeted review, active learning tasks, strategic data collection, and case study application. Final outputs are two: 1) task 1 to 4 as shown in # 🤜input2algorithm2output and 2) Angie (TA)'s optimal time allocation as shown in # ⏰time allocation.

## Core Framework
The recitation planning follows a knowledge-bridging framework where:
- **Moshe's Desire** = instructor's intended learning outcomes
- **Student Knowledge State** = current understanding levels of students
- **Knowledge Gap** = difference between Moshe's desire and student knowledge state
- **Knowledge Bridging** = activities to close this gap

## Four Weekly Tasks in table
Refer to # 🤜input2algorithm2output in project knowledge. 

## Four Weekly Tasks in words

### 🚨Task 1: Angie Shows Moshe's Desire (15 minutes)
**Objective:** Synthesize and project the instructor's intended learning outcomes in your teaching style.

**Process Steps:**
1. Create an information space by analyzing lecture transcripts and notes
2. Map this information to two axes:
   - 🧙‍♂️🍱 **Moshe's Recipe of Cuisines:** Three key theoretical concepts with visual/diagram emphasis
   - 💻🍱 **Angie's Recipe for Programming:** Code visualizations of these concepts

**Input Requirements:**
- 🗣️ Lecture transcripts (minimum 2)
- 📝 Lecture notes/slides (minimum 3)

**Output Format:**
1. Three key theoretical concepts with corresponding diagrams. DIAGRAM is the most important thing!
2. Three instructor wisdom points connecting concepts to broader principles
3. Code examples demonstrating practical application of concepts

just for example (Don't follow this example), 
```
For a linear regression topic:
- Key Concept 1: Ordinary Least Squares estimation with diagram showing minimized squared errors
- Key Concept 2: Coefficient interpretation with diagram showing slope interpretation
- Key Concept 3: Model diagnostics with residual plot visualizations
- Wisdom 1: "Models are always wrong, but some are useful" - focusing on practical application over perfection
- Wisdom 2: Understanding when simple models outperform complex ones for real-world decisions
- Wisdom 3: The importance of connecting statistical outcomes to business actions
- Programming Recipe: Python implementation showing coefficient calculation, interpretation and diagnostics
```

### 🚨Task 2: Students Learn Their Knowledge State (15 minutes)
**Objective:** Design hypothesis-driven tasks that help students assess their current understanding through application.

**Process Steps:**
1. Based on Task 1 outcomes, create real-world hypothesis scenarios requiring the week's concepts
2. Structure the task to require both theoretical understanding and implementation skills
3. Ensure task reveals knowledge gaps in a constructive way

**Input Requirements:**
- Outcomes from Task 1
- Previous recitation transcript (to understand existing student questions/challenges)

**Output Format:**
A hypothesis-driven task following the structure:
```
[Stakeholder]'s hypothesis: [Subject] are more/less likely to [action] when [condition]
```

**Requirements:**
- Must incorporate key concepts from Task 1
- Must require programming implementation
- Should be completable within 15 minutes
- Should reveal common misconceptions

**Example Execution:**
```
Transportation Planner's Hypothesis: Commuters living in high-density neighborhoods are less likely 
to drive to work when public transit stations are within 500 meters of their homes.

Task: Using provided neighborhood density and commute data:
1. Create a multivariate regression model
2. Interpret the coefficient for transit proximity 
3. Evaluate if the hypothesis is supported
4. Discuss practical significance of findings
```

### 🚨Task 3: Angie Learns Students' Knowledge State (10 minutes)
**Objective:** Design data collection methods that reveal student understanding levels and knowledge gaps.

**Process Steps:**
1. Based on outcomes from Tasks 1 and 2, identify potential knowledge gaps
2. Design exclusive in-person data collection methods that provide immediate value
3. Structure collection to maximize delta K (knowledge gain) measurement

**Input Requirements:**
- Outcomes from Tasks 1 and 2
- Previous data collection results (if available)

**Output Format:**
1. Data collection method detailed explanation
2. Implementation plan for in-class activity
3. Analysis framework for interpreting results
4. Strategy for using insights for future recitation improvement

**Key Requirements:**
- Must provide immediate value to in-person attendees
- Must be completable within 10 minutes
- Should yield actionable insights about knowledge gaps
- Should prioritize qualitative understanding over self-reported metrics

**Example Execution:**
```
Concept Mapping Challenge:
1. Provide students with partially completed concept maps connecting key regression techniques
2. Ask students to complete connections with correct relationship descriptions
3. Collect maps and digitize for analysis
4. Use patterns of incorrect connections to identify misconception trends
5. Provide immediate feedback on common errors before class ends
6. Use results to focus future recitations on identified weak points
```

### 🚨Task 4: Angie Helps Students Reach Moshe's Desire (15 minutes)
**Objective:** Connect recitation content to case study applications, providing pathways from current knowledge states to desired outcomes.

**Process Steps:**
1. Based on outcomes from Tasks 1-3, identify bridges between current knowledge and case study requirements
2. Create three concise sentences that explicitly connect concepts, tasks, and case applications
3. Develop personalized guidance based on observed knowledge states

**Input Requirements:**
- Outcomes from Tasks 1-3
- Case study materials

**Output Format:**
1. Three concise bridging sentences
2. Tailored guidance for different knowledge states
3. Specific case study application points

**Key Requirements:**
- Must explicitly connect theoretical concepts to case requirements
- Must acknowledge different starting knowledge states
- Should motivate students by highlighting practical relevance
- Should be forward-looking to upcoming case work

**Example Execution:**
```
Bridging Sentences:
1. The coefficient interpretation skills practiced in today's check-in task directly translate to how you'll need to analyze the transportation mode choice factors in section 3.2 of the case study.
2. Understanding the difference between statistical and practical significance (Moshe's second wisdom point) will be crucial when making recommendations to the city council in your case submissions.
3. The data visualization techniques from today's programming recipe provide the exact framework needed to create the required decision support graphics in section 4.1.

Additional guidance for students struggling with coefficient interpretation:
[Specific pathway to bridge this knowledge gap]
```

## Implementation Timeline
For each 55-minute recitation:
- Task 1: 15 minutes
- Task 2: 15 minutes
- Task 3: 10 minutes
- Task 4: 15 minutes

## Preparation Guidelines
Total preparation time: 10 hours
- Task 1: 2 hours (reviewing/synthesizing lecture content)
- Task 2: 2 hours (designing engaging check-in tasks)
- Task 3: 4 hours (creating data collection tools and grading focused on recitation attendees)
- Task 4: 2 hours (analyzing case study and creating connection points)

## Key Success Metrics
- Average delta K (knowledge gain) among recitation participants
- Quality of case study submissions (scores 1-5)
- Course evaluation feedback
- In-person attendance consistency

## Execution Instructions
1. Start each planning cycle by thoroughly analyzing provided lecture materials
2. Work sequentially through the four tasks
3. Ensure each task builds upon insights from previous tasks
4. Document specific observations about student knowledge states
5. Refine approach based on collected data from previous recitations

---

## Input Format Requirements for LLM Agent Implementation

When using an LLM agent for planning implementation, provide the following structured inputs:

```
# Recitation Planning Request

## Course Materials
- Lecture Transcripts: [List transcript filenames]
- Lecture Notes: [List lecture note filenames]
- Previous Recitation Data: [List previous recitation transcript]
- Case Study: [Case study filename]

## Task Instructions
1. Review class: Project information space spanned by transcripts and lecture notes to Moshe's recipe of cuisines and Angie's recipe for programming.
2. Check-in task: Design a hypothesis-driven task that students can implement with programming based on Task 1 outcomes.
3. Data collection: Design one data collection method to maximize knowledge gain measurement.
4. Preview case study: Create three sentences connecting concepts, check-in task, and case study applications.

## Special Considerations
[Any specific focus areas, challenges, or important context]
```

# ⏰time allocation

| Planning Component    | One-Sentence Instruction                                                                                                                                                                                                                                                 | Example from Your Framework                                                                                                                                                                                                                                                                        | Time Allocation                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1. Review Class       | Synthesize lecture transcripts and notes into a structured framework presenting three key theoretical concepts with visual representations (Moshe's recipe), three instructor insights (Moshe's wisdom), and corresponding programming implementations (Angie's recipe). | "Project information space spanned by 🗣️ transcript1,2 that explains 📝lecture note 1,2,3 to two axes: 🧙‍♂️🍱 moshe's recipe of cuisines (three key ideas with diagrams wrapped in three moshe's wisdom) and 💻🍱 angie's recipe for programming (code visualizations of concepts)."             | **Prep:** 2 hours<br>**Class:** 15 minutes                                                                            |
| 2. Check-in Task      | Design a hypothesis-driven real-world problem that requires students to apply the week's key concepts through programming implementation, following the pattern of your examples.                                                                                        | "Design a task like '👩🏽‍🍳chef's hypothesis: later shift 👨🏻‍🚒workers are more likely to order 🍔lunch items at 10am' or '👨🏼‍💼marketer's hypothesis: umbrella usage of 👨‍👩‍👧‍👦 boston local's during snow is lower than during ☔️ rain' that students can implement using programming." | **Prep:** 2 hours<br>**Class:** 15 minutes                                                                            |
| 3. Data Collection    | Design and implement an exclusive in-person data collection experience that provides immediate value to attendees while measuring specific knowledge gains beyond self-reported participation.                                                                           | "Design one data collection method to maximize average delta K (knowledge gain) from students participating in the recitation, improving upon previously collected self-reported participation."                                                                                                   | **Prep:** 4 hour<br>- grading to give feedback (⭐️will prioritize who attend recitation)<br><br>**Class:** 10 minutes |
| 4. Preview Case Study | Create three concise sentences that explicitly connect the theoretical concepts from lectures, the practical skills from the check-in task, and the relevant applications in the course case study.                                                                      | "Building on review class and check-in task, explain in three sentences how case study connects with the outcomes of previous components."                                                                                                                                                         | **Prep:** 2 hours<br>**Class:** 15 minutes                                                                            |
|                       | **TOTAL**                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                    | **Prep:** 10 hours<br>**Class:** 55 minutes                                                                           |

# 🤜input2algorithm2output  

| each section's desire                                                                                                              | input                                                                                                                                                                                                                                                                                                                                                                                                                  | algorithm                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | output                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| 1. review class<br><br>🚨goal1: infer moshe's desired knowledge state together                                                     | 🗣️ transcript1 and 2 <br>[[1.202 - Demand Modeling Inst.Var_otter_ai.txt]]<br>[[1.202 - Demand Modeling Time Series_otter_ai.txt]]<br> <br> 📝lecture note 1,2,3<br>[[1.202_s25_Lecture11_TimeSeriesAnalysis.pdf]]<br>[[1.202_s25_Lecture12_IV.pdf]]<br>                                                                                                                                                              | project 🗣️ transcript1,2 that explains 📝lecture note 1,2,3 to my three 🤜action space in the following three steps<br><br>1. imagine an information space spanned by 🗣️ transcript1,2 that explains 📝lecture note 1,2,3.<br><br>2. imagine two axes: 🧙‍♂️🍱 moshe's recipe of cuisines, 💻🍱 angie's recipe for  programming.<br><br>3. project the information space from 1 to the axes in 2.<br><br>outcome of 3 should provide the most efficient review of what moshe (instructor) intended students to learn about demand modeling in a format of teaching programming. <br><br>🧙‍♂️🍱 moshe's recipe of cuisines consists of💡three key ideas  (with higher preference on the concepts with diagram from 📝lecture note) wrapped in a 🧙‍♂️ three moshe's wisdom angie found interesting (moshe wants to teach us to be a chef, not instill recipe)<br><br>💻🍱 angie's recipe for  programming shows (visualizes) with code the concepts explained in class | 🚨task1: answer what is moshe's desired knowledge state?                                                          |
| 2. check-in task<br><br>🚨🚨goal2: let students infer their knowledge state<br>                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                        | building on outcome of 🚨task1,  design a task that students can digest 🧙‍♂️🍱 moshe's recipe of cuisines and implement with 💻🍱 angie's recipe for  programming.<br><br>before <br>- 👩🏽‍🍳chef's hypothesis: later shift 👨🏻‍🚒workers are more likely to order 🍔lunch items at 10am<br><br>- 👨🏼‍💼marketer's hypothesis: umbrella usage of 👨‍👩‍👧‍👦 boston local's during snow is lower than during ☔️ rain<br><br>- 🏢city council's hypothesis: citizen's car ownership are less likely to support 🚸pedestrianization than non-car owners<br><br>- 🌙amoon's hypothesis: 👨‍🎓student's 📚assignment load and 😋hungriness affect computer lab attendance                                                                                                                                                                                                                                                                                                | 🚨🚨task2: what are three prompts i should give to students to help students learn their  knowledge state?        |
| 3. discuss to collect data<br><br>🚨🚨🚨goal3: angie learns students' knowledge state                                              | 🤩angie's inference and allocation<br>1. desire: infer moshe's desired knowledge state of students (review class), infer students current knowledge state (check-in+data collection), prepare students to bridge that gap by programming case study ()<br><br>2.output measure: by your grades (customer: moshe) and course evaluation (customer: students)<br><br>3. reward: quality of case study 1~5 submission<br> | building on outcome of 🚨task1, 🚨🚨task2,  🤩angie's inference and allocation, design one data i should collect, given my goal to maximize average delta K (knowledge gain) from student participating the recitation. last class, I collected self-reported participation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 🚨🚨🚨task3: what should angie focus on when listening to student's answer to learn their knowledge state?        |
| 4. preview case study<br><br>🚨🚨🚨🚨goal4: angie helps students reach to moshe's desire from each of your knowledge state<br><br> | [[CaseStudy2_22_Solutions.pdf]]<br>[[Midterm_23_22_18_16_sol 1.pdf]]                                                                                                                                                                                                                                                                                                                                                   | building on outcome of 🚨task1, 🚨🚨task2, 🚨🚨🚨task3, explain in three sentence how i should curate case study to students to motivate them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 🚨🚨🚨🚨task4: how can angie bridge students' knowledge state with moshe's desire with programming in case study? |
