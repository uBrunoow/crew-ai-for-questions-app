from crewai import Task
from .agents import agentes, create_agent, create_revisor, create_resolutor, create_difficulty_agent


def generate_wrong_answers_task(question, correct_answer, subject):
    if subject not in agentes:
        agentes[subject] = create_agent(subject)

    return Task(
        description=f"Dada a pergunta: '{question}', gere quatro respostas erradas com base na resposta correta '{
            correct_answer}' e retorne enumerado em a) b) c) e d). Se caso a resposta correta for uma palavra curta ou uma sigla, gere respostas erradas que sejam plausíveis, mas incorretas curtas se for o caso, agora se a resposta correta for longa tente fazer o mais parecido possível. Um exemplo disso é a seguinte ocasião a resposta correta é Dezembro, as respostas erradas mais parecidas seriam os meses correto? Como Janeiro, Fevereiro, Novembro. Agora outra questão é na qual eu insiro uma resposta de matemática ou física e os números me retornam parecidos por exemplo resposta correta é 175 não gostaria que me retornasse números muito parecidos, queria uns números mais randômicos dependendo do tipo de questão, o quão mais difícil ficar para o usuário saber responder melhor.",
        agent=agentes[subject],
        expected_output="Quatro respostas erradas para a pergunta."
    )


def generate_wrong_answers_by_image_task(question, correct_answer, subject, image):
    if subject not in agentes:
        agentes[subject] = create_agent(subject)

    return Task(
        description=f"Dada a pergunta: '{question}', gere quatro respostas erradas com base na resposta correta '{correct_answer}' e retorne enumerado em a) b) c) e d). Se caso a resposta correta for uma palavra curta ou uma sigla, gere respostas erradas que sejam plausíveis, mas incorretas curtas se for o caso, agora se a resposta correta for longa tente fazer o mais parecido possível. Um exemplo disso é a seguinte ocasião a resposta correta é Dezembro, as respostas erradas mais parecidas seriam os meses correto? Como Janeiro, Fevereiro, Novembro. Agora outra questão é na qual eu insiro uma resposta de matemática ou física e os números me retornam parecidos por exemplo resposta correta é 175 não gostaria que me retornasse números muito parecidos, queria uns números mais randômicos dependendo do tipo de questão, o quão mais difícil ficar para o usuário saber responder melhor. Além disso, gere respostas erradas com base na imagem fornecida.",
        agent=agentes[subject],
        expected_output="Quatro respostas erradas para a pergunta.",
        additional_inputs={'image': image}
    )


def generate_resolutions_task(question, correct_answer, subject, incorrect_answers):
    if subject not in agentes:
        agentes[subject] = create_resolutor(subject)

    return Task(
        description=f"Dada a pergunta: '{question}', gere uma resolução com base na resposta correta '{
            correct_answer}'. Além disso, forneça uma resolução em negrito e uma explicação detalhada em um formato WYSIWYG com TAGS HTML5 sejam elas <br/> <strong/> entre outras, Troque todo ** que seria para ser o negrito pela tag <strong/> para ficar no estilo HTML5. Com o tópico bem explícito Resolução e Explicação. Também explique o porquê de ser a resposta correta e as outras alternativas ({', '.join(incorrect_answers)}) não serem as respostas corretas.",
        agent=agentes[subject],
        expected_output=(
            "<strong>Resolução:</strong> <br>"
            f"<strong>{correct_answer}</strong><br>"
            "<strong>Explicação:</strong> <br>"
            f"A resposta correta é <strong>{
                correct_answer}</strong> porque...<br>"
            f"As outras alternativas ({', '.join(
                incorrect_answers)}) não são corretas porque..."
        )
    )


def revision_answers_task(question, correct_answer, subject):
    if subject not in agentes:
        agentes[subject] = create_revisor(subject)

    return Task(
        description=f"Dada a pergunta: '{question}', baseada na resposta correta '{
            correct_answer}', verifique se esta é realmente a resposta correta. Caso não seja, retorne a resposta correta e justifique o porquê. Se for a resposta correta, retorne a justificativa de porquê é a resposta correta.",
        agent=agentes[subject],
        expected_output="Resposta Correta: [texto explicativo] ou Resposta Incorreta: [justificativa]"
    )


def generate_difficulty_task(question, correct_answer, subject):
    if subject not in agentes:
        agentes[subject] = create_difficulty_agent(subject)

    return Task(
        description=f"Dada a pergunta: '{question}', gere um nível de dificuldade para a questão entre (1, \"Muito Fácil\"), (2, \"Fácil\"), (3, \"Médio\"), (4, \"Difícil\"), (5, \"Muito Difícil\"). baseado na resposta correta '{
            correct_answer}'. Retorne apenas o número do nível de dificuldade.",
        agent=agentes[subject],
        expected_output="Número do nível de dificuldade da questão."
    )
