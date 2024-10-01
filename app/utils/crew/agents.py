import os
from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv('GOOGLE_API_KEY'))


def create_agent(materia):
    return Agent(
        role=f"Gerador de Respostas Erradas de {materia}",
        goal=f"Gerar respostas incorretas para perguntas de {materia}",
        verbose=True,
        memory=True,
        backstory=(
            f"Como uma IA projetada para gerar respostas plausíveis, mas incorretas,"
            f"você fornece respostas criativas e enganosas para perguntas de {
                materia},"
            f"garantindo que sejam críveis, mas incorretas."
        ),
        llm=llm,
        allow_delegation=False
    )


def create_wrong_answers_agent(materia):
    return Agent(
        role=f"Gerador de Respostas Erradas de {materia}",
        goal=f"Gerar respostas incorretas para perguntas de {
            materia} baseadas no enunciado da questão e na imagem fornecida",
        verbose=True,
        memory=True,
        backstory=(
            f"Como uma IA projetada para gerar respostas plausíveis, mas incorretas,"
            f"você fornece respostas criativas e enganosas para perguntas de {
                materia},"
            f"garantindo que sejam críveis, mas incorretas. Você deve considerar tanto o enunciado da questão quanto a imagem fornecida."
        ),
        llm=llm,
        allow_delegation=False
    )


def create_resolutor(materia):
    return Agent(
        role=f"Resolutor de Questões de {materia}",
        goal=f"Resolver questões de {materia}",
        verbose=True,
        memory=True,
        backstory=(
            f"Como uma IA projetada para resolver questões, você verifica se a resposta"
            f"está correta ou não. Caso a resposta esteja correta, você justifica o porquê."
            f"Se a resposta estiver incorreta, você retorna a resposta correta e justifica o porquê."
        ),
        llm=llm,
        allow_delegation=False
    )


def create_revisor(materia):
    return Agent(
        role=f"Revisor de Respostas de {materia}",
        goal=f"Revisar respostas de {materia}",
        verbose=True,
        memory=True,
        backstory=(
            f"Como uma IA projetada para revisar respostas, você verifica se a resposta"
            f"está correta ou não. Caso a resposta esteja correta, você justifica o porquê."
            f"Se a resposta estiver incorreta, você retorna a resposta correta e justifica o porquê."
        ),
        llm=llm,
        allow_delegation=False
    )


def create_difficulty_agent(materia):
    return Agent(
        role=f"Gerador de Dificuldade de Questões de {materia}",
        goal=f"Gerar um nível de dificuldade para questões de {materia}",
        verbose=True,
        memory=True,
        backstory=(
            f"Como uma IA projetada para gerar um nível de dificuldade para questões de {
                materia},"
            f"você deve considerar a complexidade da questão e a quantidade de informações"
            f"necessárias para resolvê-la."
        ),
        llm=llm,
        allow_delegation=False
    )


agentes = {}
