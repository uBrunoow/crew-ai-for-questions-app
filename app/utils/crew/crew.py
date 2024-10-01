from crewai import Crew
from .agents import agentes, create_agent, create_revisor, create_difficulty_agent
from .tasks import (
    generate_wrong_answers_task,
    revision_answers_task,
    generate_resolutions_task,
    generate_wrong_answers_by_image_task,
    generate_difficulty_task
)


def wrong_answers_crew(question, correct_answer, subject):
    if subject not in agentes:
        agentes[subject] = create_agent(subject)

    crew = Crew(
        agents=[agentes[subject]],
        tasks=[generate_wrong_answers_task(
            question=question, correct_answer=correct_answer, subject=subject)]
    )
    result = crew.kickoff()
    # Supondo que o resultado seja uma lista de respostas erradas
    return result


def wrong_answers_by_image_crew(question, correct_answer, subject, image):
    if subject not in agentes:
        agentes[subject] = create_agent(subject)

    crew = Crew(
        agents=[agentes[subject]],
        tasks=[generate_wrong_answers_by_image_task(
            question=question, correct_answer=correct_answer, subject=subject, image=image)]
    )
    result = crew.kickoff()
    # Supondo que o resultado seja uma lista de respostas erradas
    return result


def resolutions_crew(question, correct_answer, subject, incorrect_answers):
    if subject not in agentes:
        agentes[subject] = create_agent(subject)

    crew = Crew(
        agents=[agentes[subject]],
        tasks=[generate_resolutions_task(
            question=question, correct_answer=correct_answer, subject=subject, incorrect_answers=incorrect_answers)]
    )
    result = crew.kickoff()
    # Supondo que o resultado seja uma resolução
    return result


def revision_answers_crew(question, correct_answer, subject):
    if subject not in agentes:
        agentes[subject] = create_revisor(subject)

    crew = Crew(
        agents=[agentes[subject]],
        tasks=[revision_answers_task(
            question=question, correct_answer=correct_answer, subject=subject)]
    )
    result = crew.kickoff()
    # Supondo que o resultado seja uma lista de respostas erradas
    return result


def difficulty_crew(question, correct_answer, subject):
    if subject not in agentes:
        agentes[subject] = create_difficulty_agent(subject)

    crew = Crew(
        agents=[agentes[subject]],
        tasks=[generate_difficulty_task(
            question=question, correct_answer=correct_answer, subject=subject)]
    )
    result = crew.kickoff()
    # Supondo que o resultado seja uma lista de respostas erradas
    return result
