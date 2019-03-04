import scripts.question_scripts as question_scripts
import maths_scripts.mechanics.base_2d as base_2d
import random


def find_resultant_of_two_forces(name: str, difficulty: int) -> question_scripts.Question:
    type_id = 1
    obj = base_2d.BasicObject()
    force_magnitude_1 = random.randint(1, 100)
    force_direction_1 = random.randint(0, 360)
    obj.add_force(force_magnitude_1, force_direction_1)
    force_magnitude_2 = random.randint(1, 100)
    force_direction_2 = random.randint(0, 360)
    obj.add_force(force_magnitude_2, force_direction_2)
    question_to_ask = random.randint(1, 2)
    if question_to_ask == 1:
        question_text = 'A force P acts on an object on a frictionless plane with magnitude {}N in the direction {}° ' \
                        'to the x axis and another force, Q acts with magnitude {}N in the direction {}° to the x ' \
                        'axis. ' \
                        'Find the magnitude of the resultant force.'.format(force_magnitude_1,
                                                                            force_direction_1,
                                                                            force_magnitude_2,
                                                                            force_direction_2)
        correct_answer = obj.force
        question = question_scripts.Question(name, type_id, difficulty, question_text, correct_answer)
        return question
    elif question_to_ask == 2:
        question_text = 'A force P acts on an object on a frictionless plane with magnitude {}N in the direction {}° ' \
                        'to the x axis and another force, Q acts with magnitude {}N in the direction {}° to the x ' \
                        'axis. ' \
                        'Find the direction relative to the x axis of the resultant force.'.format(force_magnitude_1,
                                                                                                   force_direction_1,
                                                                                                   force_magnitude_2,
                                                                                                   force_direction_2)
        correct_answer = obj.force_direction
        question = question_scripts.Question(name, type_id, difficulty, question_text, correct_answer)
        return question
    raise RuntimeError


if __name__ == '__main__':
    q = find_resultant_of_two_forces('fefe', 4)
    print(q.question_text)
    print(q.correct_answer)
    print(q.answer_b)
    print(q.answer_c)
    print(q.answer_d)
