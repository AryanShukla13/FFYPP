from sessional.models import Sessional, Question, QuestionStudentMapping

class SessionalService:
    @staticmethod
    def calculate_average_co(sessional_id, co):
        sessional = Sessional.objects.get(id=sessional_id)
        questions = Question.objects.filter(sessional=sessional, co=co)
        average_list = []

        for question in questions:
            students_mapping = QuestionStudentMapping.objects.filter(question=question)
            total_students = 0
            total_students_above_target = 0

            for mapping in students_mapping:
                if question.maximum_marks == 2:
                    target = 1.56
                if question.maximum_marks == 5:
                    target = 3.9
                if question.maximum_marks == 9:
                    target = 7.02

                if mapping.marks_obtained >= target:
                    total_students_above_target += 1
                total_students += 1

            average_for_question = (total_students_above_target)/(total_students)*100
            average_list.append(average_for_question)

        result = 0
        for average in average_list:
            result += average

        result = result/len(average_list)
        return result
        