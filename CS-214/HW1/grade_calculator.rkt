#lang dssl2

let eight_principles = ["Know your rights.",
    "Acknowledge your sources.",
    "Protect your work.",
    "Avoid suspicion.",
    "Do your own work.",
    "Never falsify a record or permit another person to do so.",
    "Never fabricate data, citations, or experimental results.",
    "Always tell the truth when discussing your work with your instructor."]

# HW1: Grade Calculator
    
###
### Data Definitions
###

struct homework:
    let n_passed_test_suites: int?
    let self_eval_percentage: num?
    let mutation_percentage:  OrC(num?, NoneC) # no mutation testing for hw1

struct project:
    let n_passed_test_suites:      int?
    let design_docs_satisfactory?: VecKC[bool?, bool?, bool?]

let track_grades  = ["F","D","C","B","A"]
let letter_grades = ["F","D","D+","C-","C","C+","B-","B","B+","A-","A"]

# We will see this function again in the complexity lecture; stay tuned!
def linear_search (elements: VecC[AnyC], target):
    for x in elements:
        if x == target: return True
    return False
def track_grade?  (str): return linear_search(track_grades,  str)
def letter_grade? (str): return linear_search(letter_grades, str)

def loop_count(vec: VecC[AnyC], f: FunC[AnyC, bool?]) -> int?:
    let count = 0
    for b in vec:
        if f(b): 
            count = count + 1
    return count

def score_to_letter(lst: VecC[int?], score: int?) -> track_grade?:
    for i in range(0, len(lst), 1):
        if score >= lst[i]:
            return track_grades[4-i]
    return track_grades[0]

###
### Tracks
###

def integration_grade(project_score: int?) -> track_grade?:
    if not project_score >=0 or not project_score <=6:
        error('score out of range')  
    return score_to_letter([6, 4, 3, 2], project_score)
    

test 'first integration_grade test; you will need to add more':
    assert_error integration_grade(7), "score out of range"
    assert_error integration_grade(6.1), "contract violation"
    assert integration_grade(6) == 'A'
    assert integration_grade(5) == 'B' and integration_grade(4) == 'B'
    assert integration_grade(3) == 'C'
    assert integration_grade(2) == 'D'
    assert integration_grade(1) == 'F' and integration_grade(0) == 'F'

def implementation_grade(homework_scores: VecC[int?]) -> track_grade?:
    if not len(homework_scores) == 5:
        error("incorrect number of assignments")
    
    let total = 0
    for i in homework_scores:
        if not i >=0 or not i <=4:
            error("score out of range")
        total = total + i
     
    if not total >=0 or not total <=20:
        error("score out of range")
    return score_to_letter([20, 16, 12, 10], total)

test 'first implementation_grade test; you will need to add more':
    assert_error implementation_grade([0,5,0]), "incorrect number of assignments"
    assert_error implementation_grade([5, -1, 0, 0, 0]), "score out of range"
    
    assert implementation_grade([4,4,4,4,4]) == "A"
    assert implementation_grade([4,4,4,4,3]) == "B" and implementation_grade([4,4,4,4,0]) == "B"
    assert implementation_grade([4,4,4,0,0]) == "C" and implementation_grade([4,4,4,3,0]) == "C"
    assert implementation_grade([4,4,2,0,0]) == "D" and implementation_grade([4,4,3,0,0]) == "D"
    assert implementation_grade([0,0,0,0,0]) == "F" and implementation_grade([4,4,1,0,0]) == "F"

def exams_theory_points(exam1_score: num?, exam2_score: num?) -> int?:
    let total = 0
    if not (exam1_score >=0 and exam1_score <=1) or not (exam2_score >=0 and exam2_score <=1):
        error("score out of range")
    for i in [exam1_score, exam2_score]:
        if i <0.35:
            total = total+0
        elif i <0.55:
            total = total+1
        elif i <0.7:
            total = total+2
        elif i <0.85:
            total = total+3
        else:
            total = total+4
    return total

test 'first exams_theory_points test; you will need to add more':
    assert_error exams_theory_points(0.0, 1.1), "score out of range"
    
    assert exams_theory_points(0.85, 1) == 8
    assert exams_theory_points(0.7, 0.85) == 7
    assert exams_theory_points(0.7, 0.84) == 6
    assert exams_theory_points(0.55, 0.7) == 5
    assert exams_theory_points(0.55, 0.69) == 4
    assert exams_theory_points(0.35,0.55) == 3
    assert exams_theory_points(0.35, 0.54) == 2
    assert exams_theory_points(0, 0.35) == 1
    assert exams_theory_points(0, 0.34) == 0

def theory_grade(theory_points: int?) -> track_grade?:
    return score_to_letter([13, 11, 9, 8], theory_points)

def tally_design_points(assignments: VecC[AnyC],
                        expected_n_assignments: int?,
                        counts?: FunC[AnyC, bool?]) -> int?:
    if expected_n_assignments != len(assignments):
        error("incorrect number of assignments")
    return loop_count(assignments, counts?)

##NEEDS TESTS

def self_evals_design_points(self_eval_scores: VecC[num?]) -> int?:
    if not 5 == len(self_eval_scores):
        error("incorrect number of assignments")
    return loop_count(self_eval_scores, lambda x: x>=0.5)
   
test 'self_evals_design_points testing':
    assert_error self_evals_design_points([0,0,0,0,0,0]), "incorrect number of assignments"
    
    assert self_evals_design_points([0,0,0,0,-1]) == 0
    assert self_evals_design_points([0,0,0,0,0.5]) == 1
    assert self_evals_design_points([0,-1,10,1,0.5]) == 3

def mutation_testing_design_points(mutation_scores: VecC[num?]) -> int?:
    if not 4 == len(mutation_scores):
        error("incorrect number of assignments")
    return loop_count(mutation_scores, lambda x: x>=0.5)

test 'mutation_testing_design_points testing':
    assert_error mutation_testing_design_points([0,0,0,0,0,0]), "incorrect number of assignments"
    
    assert mutation_testing_design_points([0,0,0,-1]) == 0
    assert mutation_testing_design_points([0,0,0,0.5]) == 1
    assert mutation_testing_design_points([-1,10,1,0.5]) == 3
    assert mutation_testing_design_points([0.3, 0.6, 0.8, 1.0]) == 3

def design_docs_design_points(design_docs_scores: VecC[bool?]) -> int?:
    if not 3 == len(design_docs_scores):
        error("incorrect number of assignments")
    return loop_count(design_docs_scores, lambda x: x==True)

test "design_docs_design_points":
    assert_error design_docs_design_points([]), "incorrect number of assignments"
    
    assert design_docs_design_points([False, False, False]) == 0
    assert design_docs_design_points([True, True, True]) == 3

def interviews_design_points(interviews_scores: VecC[bool?]) -> int?:
    return design_docs_design_points(interviews_scores)
    

def design_grade(design_points: int?) -> track_grade?:
    return score_to_letter([14, 12, 10, 8], design_points)

###
### Final Grades
###

def index_of (elt: AnyC, v: VecC[AnyC]) -> int?:
    for i, x in v:
        if elt == x: return i
    error('element not found: %p', elt)

# Returns `True` if grade `g1` is less than grade `g2`; otherwise `False`.
# This function is a *custom comparator*. We will see those again in the
# sorting lecture.
def grade_lt (g1: letter_grade?, g2: letter_grade?) -> bool?:
    return index_of(g1, letter_grades) < index_of(g2, letter_grades)

let TracksC = VecKC[track_grade?, track_grade?, track_grade?, track_grade?]

def base_grade (tracks: TracksC) -> letter_grade?:
    let cur_lowest = tracks[0]
    for track in tracks:
        if grade_lt(track, cur_lowest):
            cur_lowest = track
    return cur_lowest
    
    
def n_above_expectations (tracks: TracksC) -> int?:
    let total = 0
    let lowest = base_grade(tracks)
    for track in tracks:
        if grade_lt(lowest, track):
            total = total + 1
    #let total2 = loop_count(tracks, lambda x, y: grade_lt(x,y))
    #assert total2 == total
    #couldn't figure this out, will be asking about it in office hours
    return total
            

def final_grade (base_grade: track_grade?,
                 n_above_expectations: int?) -> letter_grade?:
    let ind = index_of(base_grade,letter_grades)
    ind = ind+ n_above_expectations
    if ind > 10:
        ind = 10
    return letter_grades[ind]

###
### Students
###

class Student:
    let name: str?
    let homeworks: VecKC[homework?, homework?, homework?, homework?, homework?]
    let interviews_satisfactory?: VecKC[bool?, bool?, bool?]
    let project: project?
    let worksheet_scores: VecKC[num?, num?, num?, num?, num?]
    let exam_scores: VecKC[num?, num?]

    def __init__ (self, name, homeworks, interviews, project,
                  worksheet_scores, exam_scores):
        self.name = name
        self.homeworks = homeworks
        self.interviews_satisfactory? = interviews
        self.project = project
        self.worksheet_scores = worksheet_scores
        self.exam_scores = exam_scores

    def get_homework_grades(self) -> VecC[int?]:
        let return_vec = [None;len(self.homeworks)]
        for ind in range(len(self.homeworks)):
            let hw = self.homeworks[ind]
            return_vec[ind] = hw.n_passed_test_suites
        return return_vec

    def get_project_grade(self) -> int?:
        return self.project.n_passed_test_suites

    def resubmit_homework (self, n: int?, new_grade: int?) -> NoneC:
        if not (n>0 and n < 6):
            error("no such homework")
        if new_grade > self.homeworks[n-1].n_passed_test_suites:
            self.homeworks[n-1].n_passed_test_suites = new_grade

    def resubmit_project (self, new_grade: int?) -> NoneC:
        if new_grade > self.project.n_passed_test_suites:
            self.project.n_passed_test_suites = new_grade

    # Determine a student's final letter grade from their body of work in the
    # class (i.e., the fields) using the helper functions you wrote earlier.
    def letter_grade (self) -> letter_grade?:
        let implementation = implementation_grade(self.get_homework_grades())
        let integration = integration_grade(self.project.n_passed_test_suites)
        # Theory grade
        let worksheets = 0
        for w in self.worksheet_scores:
            if w == 1.0: worksheets = worksheets + 1
        let exams = exams_theory_points(self.exam_scores[0], self.exam_scores[1])
        let theory = theory_grade(worksheets + exams)
        # Design grade
        let self_evals = [h.self_eval_percentage for h in self.homeworks]
        let self_eval_points = self_evals_design_points(self_evals)
        let mutation = [h.mutation_percentage for h in self.homeworks
                        if h.mutation_percentage is not None]
        let mutation_points = mutation_testing_design_points(mutation)
        let design_docs = self.project.design_docs_satisfactory?
        let doc_points = design_docs_design_points(design_docs)
        let interviews = self.interviews_satisfactory?
        let interview_points = interviews_design_points(interviews)
        let design_points = self_eval_points + mutation_points + doc_points \
                            + interview_points
        let design = design_grade(design_points)
        # Final grade
        let tracks = [implementation, integration, theory, design]
        let base = base_grade(tracks)
        let above = n_above_expectations(tracks)
        return final_grade(base, above)

###
### Another paltry couple tests
###


    
test 'Student#letter_grade, worst case scenario':
    let s = Student('Everyone, right now',
                    [homework(0, 0.0, None),
                     homework(0, 0.0, 0.0),
                     homework(0, 0.0, 0.0),
                     homework(0, 0.0, 0.0),
                     homework(0, 0.0, 0.0)],
                    [False, False, False],
                    project(0, [False, False, False]),
                    [0.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0])
    assert s.letter_grade() == 'F'
    
    

test 'Student#letter_grade, best case scenario':
    let s = Student("You, if you work harder than you've ever worked",
                    [homework(4, 1.0, None),
                     homework(4, 1.0, 1.0),
                     homework(4, 1.0, 1.0),
                     homework(4, 1.0, 1.0),
                     homework(4, 1.0, 1.0)],
                    [True, True, True],
                    project(6, [True, True, True]),
                    [1.0, 1.0, 1.0, 1.0, 1.0],
                    [1.0, 1.0])
    assert s.letter_grade() == 'A'

test 'testing student functions':
    let s = Student('nerd',
                    [homework(3, 0.8, None),
                     homework(2, 0.6, 1.0),
                     homework(1, 0.2, 1.0),
                     homework(4, 0.2, 1.0),
                     homework(4, 0.6, 1.0)],
                    [False, False, False],
                    project(3, [False, False, False]),
                    [0.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0])
    assert s.get_homework_grades() == [3, 2, 1, 4, 4]
    assert s.get_project_grade() == 3
    s.resubmit_homework(1, 4)
    assert_error s.resubmit_homework(0, 4), "no such homework"
    assert s.get_homework_grades() == [4, 2, 1, 4, 4]
    s.resubmit_homework(1, 2)
    assert s.get_homework_grades() == [4, 2, 1, 4, 4]
    s.resubmit_project(1)
    assert s.get_project_grade() == 3
    s.resubmit_project(6)
    assert s.get_project_grade() == 6
    assert s.letter_grade() == "D+"