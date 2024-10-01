from django.core.management.base import BaseCommand
from questions.models import University


class Command(BaseCommand):
    help = 'Add predefined universities to the database'

    def handle(self, *args, **kwargs):
        universities = [
            {"name": "IFAC - Instituto Federal do Acre"},
            {"name": "UFAC - Universidade Federal do Acre"},
            {"name": "FADISI - Faculdade Diocesana São José"},
            {"name": "UNAMA - Universidade da Amazônia"},
            {"name": "UNESA - Universidade Estácio de Sá"},
            {"name": "UNINTER - Grupo Educacional Uninter"},
            {"name": "UNEAL - Universidade Estadual de Alagoas"},
            {"name": "UNCIASAL - Universidade Estadual de Ciências da Saúde de Alagoas"},
            {"name": "IFAL - Instituto Federal de Alagoas"},
            {"name": "UFAL - Universidade Federal de Alagoas"},
            {"name": "CESMAC - Centro de Estudos Superiores de Maceió"},
            {"name": "FAP - Faculdade Pitágoras"},
            {"name": "FITS - Faculdade Integrada Tiradentes"},
            {"name": "UEAP - Universidade Estadual do Amapá"},
            {"name": "IFAP - Instituto Federal do Amapá"},
            {"name": "UNIFAP - Universidade Federal do Amapá"},
            {"name": "CEAP - Centro de Ensino Superior do Amapá"},
            {"name": "UEA - Universidade do Estado do Amazonas"},
            {"name": "IFAM - Instituto Federal do Amazonas"},
            {"name": "UFAM - Universidade Federal do Amazonas"},
            {"name": "INPA - Instituto Nacional de Pesquisas da Amazônia"},
            {"name": "ULBRA - Universidade Luterana do Brasil"},
            {"name": "UNINILTONLINS - Universidade Nilton Lins"},
            {"name": "Fametro - Faculdade Metropolitana de Manaus"},
            {"name": "Uninorte - Centro Universitário do Norte"},
            {"name": "Unip - Universidade Paulista"},
            {"name": "UECE - Universidade Estadual do Ceará"},
            {"name": "URCA - Universidade Regional do Cariri"},
            {"name": "UVA - Universidade Estadual Vale do Acaraú"},
            {"name": "IFCE - Instituto Federal do Ceará"},
            {"name": "UFC - Universidade Federal do Ceará"},
            {"name": "UNILAB - Universidade Federal de Integração Luso-Afro-Brasileira"},
            {"name": "UFCA - Universidade Federal do Cariri"},
            {"name": "FCC - Faculdade Católica do Ceará"},
            {"name": "FCF - Faculdade Católica de Fortaleza"},
            {"name": "FCRS - Faculdade Católica Rainha do Sertão"},
            {"name": "UNICHRISTUS - Centro Universitário Christus"},
            {"name": "UNIFAMETRO - Centro Universitário Fametro"},
            {"name": "UNIFOR - Universidade de Fortaleza"},
            {"name": "UNICATÓLICA - Centro Universitário Católica de Quixadá"},
            {"name": "FA7 - Faculdade 7 de Setembro"},
            {"name": "FFB - Faculdade Farias Brito"},
            {"name": "FLF - Faculdade Luciano Feijão"},
            {"name": "Unifametro - Centro Universitário Fametro"},
            {"name": "UnDF - Universidade do Distrito Federal Jorge Amaury"},
            {"name": "IFB - Instituto Federal de Brasília"},
            {"name": "UnB - Universidade de Brasília"},
            {"name": "ENAP - Escola Nacional de Administração Pública"},
            {"name": "UCB - Universidade Católica de Brasília"},
            {"name": "SENAI - Serviço Nacional de Aprendizagem Industrial"},
            {"name": "CEUB - Centro Universitário de Brasília"},
            {"name": "FACITEC - Faculdade de Ciências Sociais e Tecnológicas"},
            {"name": "FTB - Faculdades Integradas da Terra de Brasília"},
            {"name": "IESB - Instituto de Educação Superior de Brasília"},
            {"name": "SENAC - Faculdade Senac - Distrito Federal"},
            {"name": "UNIEURO - Centro Universitário Euroamericano"},
            {"name": "UNIP - Universidade Paulista"},
            {"name": "UNOPAR - Universidade Norte do Paraná"},
            {"name": "FAPRO - Faculdade Projeção"},
            {"name": "FACELI - Faculdade de Ensino Superior de Linhares"},
            {"name": "UnAC - Universidade Aberta Capixaba"},
            {"name": "IFES - Instituto Federal do Espírito Santo"},
            {"name": "UFES - Universidade Federal do Espírito Santo"},
            {"name": "EMESCAM - Escola Superior de Ciências da Santa Casa de Misericórdia de Vitória"},
            {"name": "CUSC - Centro Universitário São Camilo"},
            {"name": "DOCTUM - Rede de Ensino Doctum"},
            {"name": "FDV - Faculdades Integradas de Vitória"},
            {"name": "FUCAPE - FUCAPE Business School"},
            {"name": "UNESA - Universidade Estácio de Sá"},
            {"name": "UniRV (FESURV) - Universidade de Rio Verde"},
            {"name": "UEG - Universidade Estadual de Goiás"},
            {"name": "IFG - Instituto Federal de Goiás"},
            {"name": "UFG - Universidade Federal de Goiás"},
            {"name": "IF Goiano - Instituto Federal Goiano"},
            {"name": "PUC - Pontifícia Universidade Católica de Goiás"},
            {"name": "UNIVERSO - Universidade Salgado de Oliveira"},
            {"name": "ULBRA - Universidade Luterana do Brasil"},
            {"name": "ALFA - Faculdade Alves Faria"},
            {"name": "FACEG - Faculdade Evangelica de Goianesia"},
            {"name": "UNESA - Universidade Estácio de Sá"},
            {"name": "UNIP - Universidade Paulista"},
            {"name": "UNIFASC - Faculdade Santa Rita de Cássia"},
            {"name": "IAESUP - Faculdades e Colégio Aphonsiano"},
            {"name": "UEMA - Universidade Estadual do Maranhão"},
            {"name": "UEMASUL - Universidade Estadual da Região Tocantina do Maranhão"},
            {"name": "IEMA - Instituto Estadual do Maranhão"},
            {"name": "IFMA - Instituto Federal do Maranhão"},
            {"name": "UFMA - Universidade Federal do Maranhão"},
            {"name": "CEST - Faculdade Santa Terezinha (São Luís)"},
            {"name": "FACIMP - Faculdade de Imperatriz"},
            {"name": "UNEMAT - Universidade do Estado de Mato Grosso"},
            {"name": "IFMT - Instituto Federal do Mato Grosso"},
            {"name": "UFMT - Universidade Federal de Mato Grosso"},
            {"name": "UFR - Universidade Federal de Rondonópolis"},
            {"name": "IPE - Instituto Parecis de Ensino, Desenvolvimento e Pesquisa"},
            {"name": "UEMS - Universidade Estadual do Mato Grosso do Sul"},
            {"name": "UFGD - Universidade Federal da Grande Dourados"},
            {"name": "IFMS - Instituto Federal de Mato Grosso do Sul"},
            {"name": "UFMS - Universidade Federal do Mato Grosso do Sul"},
            {"name": "UCDB - Universidade Católica Dom Bosco"},
            {"name": "UNIGRAN - Centro Universitário da Grande Dourados"},
            {"name": "FJP - Fundação João Pinheiro"},
            {"name": "UEMG - Universidade do Estado de Minas Gerais"},
            {"name": "UNIMONTES - Universidade Estadual de Montes Claros"},
            {"name": "CEFET-MG - Centro Federal de Educação Tecnológica de Minas Gerais"},
            {"name": "IFMG - Instituto Federal de Minas Gerais"},
            {"name": "IFNMG - Instituto Federal do Norte de Minas Gerais"},
            {"name": "IFSUDESTEMG - Instituto Federal do Sudeste de Minas"},
            {"name": "IFsULDEMINAS - Instituto Federal do Sul de Minas"},
            {"name": "IFTM - Instituto Federal do Triângulo Mineiro"},
            {"name": "UFJF - Universidade Federal de Juiz de Fora"},
            {"name": "UFLA - Universidade Federal de Lavras"},
            {"name": "UFMG - Universidade Federal de Minas Gerais"},
            {"name": "UFOP - Universidade Federal de Ouro Preto"},
            {"name": "UFSJ - Universidade Federal de São João del-Rei"},
            {"name": "UFTM - Universidade Federal do Triângulo Mineiro"},
            {"name": "UFU - Universidade Federal de Uberlândia"},
            {"name": "UFV - Universidade Federal de Viçosa"},
            {"name": "UFVJM - Universidade Federal dos Vales do Jequitinhonha e Mucuri"},
            {"name": "UNIFAL - Universidade Federal de Alfenas"},
            {"name": "UNIFEI - Universidade Federal de Itajubá"},
            {"name": "ESDHC - Escola Superior Dom Helder Câmara"},
            {"name": "FACSFX - Faculdade São Francisco Xavier"},
            {"name": "FADIPA - Faculdade de Direito de Ipatinga"},
            {"name": "FAC - Faculdade Arquidiocesana de Curvelo"},
            {"name": "FAP - Faculdade Arquidiocesana de Pirapora"},
            {"name": "FAC FUNAM - Faculdade de Tecnologia Alto e Médio São Francisco"},
            {"name": "FAZU - Faculdades Associadas de Uberaba"},
            {"name": "FCMMG - Faculdade de Ciências Médicas de Minas Gerais"},
            {"name": "FCMS/JF - Faculdade de Ciências Médicas e da Saúde de Juiz de Fora"},
            {"name": "FMG - Faculdade Metodista Granbery"},
            {"name": "FUNJOB - Faculdade de Medicina de Barbacena"},
            {"name": "FUMEC - Fundação Mineira de Educação e Cultura"},
            {"name": "INATEL - Instituto Nacional de Telecomunicações"},
            {"name": "PUCMG - Pontifícia Universidade Católica de Minas Gerais"},
            {"name": "UIT - Universidade de Itaúna"},
            {"name": "UNIBH - Centro Universitário de Belo Horizonte"},
            {"name": "UNILESTE - Centro Universitário Católica do Leste de Minas Gerais"},
            {"name": "UNIPAC - Universidade Presidente Antônio Carlos"},
            {"name": "UNIUBE - Universidade de Uberaba"},
            {"name": "UNIVAS - Universidade do Vale do Sapucaí"},
            {"name": "UNIVALE - Universidade Vale do Rio Doce"},
            {"name": "UNINCOR - Universidade Vale do Rio Verde"},
            {"name": "UNIVERSO - Universidade Salgado de Oliveira"},
            {"name": "IMIH - Instituto Metodista Izabela Hendrix"},
            {"name": "DOCTUM - Rede de Ensino Doctum"},
            {"name": "FACIC - Faculdade de Ciências Humanas de Curvelo"},
            {"name": "FACSUM - Faculdade do Sudeste Mineiro"},
            {"name": "FACTU - Faculdade de Ciências e Tecnologia de Unaí"},
            {"name": "FAF - Faculdade de Frutal"},
            {"name": "FAJANSSEN - Faculdade Arnaldo Jessen"},
            {"name": "FAVENORTE - Instituto Superior de Educação Verde Norte"},
            {"name": "FMC - Faculdades Milton Campos"},
            {"name": "FUC - Faculdades Unificadas de Cataguases"},
            {"name": "IPTAN - Instituto de Ensino Superior Presidente Tancredo Neves"},
            {"name": "UNA - Centro Universitário UNA"},
            {"name": "UNEC - Centro Universitário de Caratinga"},
            {"name": "UFRA - Universidade Federal Rural da Amazônia"},
            {"name": "UFPA - Universidade Federal do Pará"},
            {"name": "IFPA - Instituto Federal do Pará"},
            {"name": "UFOPA - Universidade Federal do Oeste do Pará"},
            {"name": "UNIFESSPA - Universidade Federal do Sul e Sudeste do Pará"},
            {"name": "UEPA - Universidade do Estado do Pará"},
            {"name": "CIABA - Centro de Instrução Almirante Braz de Aguiar"},
            {"name": "CEAMA - Centro de Educação da Amazônia"},
            {"name": "CESUPA - Centro Universitário do Estado do Pará"},
            {"name": "ESMAC - Escola Superior Madre Celeste"},
            {"name": "FAMAZ - Faculdade Metropolitana da Amazônia"},
            {"name": "FABEL - Faculdade de Belém"},
            {"name": "FACBEL - Faculdade Católica de Belém"},
            {"name": "FACIP - Faculdade Ipiranga"},
            {"name": "FAPAN - Faculdade Pan Amazônica"},
            {"name": "FEAPA - Faculdade de Estudos Avançados do Pará"},
            {"name": "FIBRA - Faculdade Integrada Brasil Amazônia"},
            {"name": "UNAMA - Universidade da Amazônia"},
            {"name": "UNIP - Universidade Paulista"},
            {"name": "UEPB - Universidade Estadual da Paraíba"},
            {"name": "IFPB - Instituto Federal da Paraíba"},
            {"name": "UFPB - Universidade Federal da Paraíba"},
            {"name": "UFCG - Universidade Federal de Campina Grande"},
            {"name": "UNIPÊ - Centro Universitário de João Pessoa"},
            {"name": "Uniuv - Centro Universitário de União da Vitória"},
            {"name": "ESBJ - Faculdade Maurício de Nassau"},
            {"name": "UNIBRASIL - Centro Universitário Autônomo do Brasil"},
            {"name": "FAVAP - Faculdades Vale do Piancó"},
            {"name": "IESP - Instituto de Educação Superior da Paraíba"},
            {"name": "UNIFIP - Centro Universitário de Patos"},
            {"name": "UNIFACISA - Centro Universitário Facisa"},
            {"name": "UNESPAR - Universidade Estadual do Paraná"},
            {"name": "UEL - Universidade Estadual de Londrina"},
            {"name": "UEM - Universidade Estadual de Maringá"},
            {"name": "UENP - Universidade Estadual do Norte do Paraná"},
            {"name": "UEPG - Universidade Estadual de Ponta Grossa"},
            {"name": "UNICENTRO - Universidade Estadual do Centro-Oeste"},
            {"name": "UNIOESTE - Universidade Estadual do Oeste do Paraná"},
            {"name": "IFPR - Instituto Federal do Paraná"},
            {"name": "UTFPR - Universidade Tecnológica Federal do Paraná"},
            {"name": "UFPR - Universidade Federal do Paraná"},
            {"name": "UNILA - Universidade Federal da Integração Latino-Americana"},
            {"name": "UFFS - Universidade Federal da Fronteira Sul"},
            {"name": "FAE - FAE Centro Universitário"},
            {"name": "FAG - Fundação Assis Gurgacz"},
            {"name": "FEPAR - Faculdade Evangélica do Paraná"},
            {"name": "FTSA - Faculdade Teológica Sul Americana"},
            {"name": "PUCPR - Pontifícia Universidade Católica do Paraná"},
            {"name": "UNIFIL - Centro Universitário Filadélfia"},
            {"name": "Univel - União Educacional de Cascavel"},
            {"name": "UNINGÁ - Faculdade Ingá"},
            {"name": "CAMPO REAL - Faculdade Campo Real"},
            {"name": "CESCAGE - Centro de Ensino Superior dos Campos Gerais"},
            {"name": "FAG - Faculdade Guairacá"},
            {"name": "FAJAR - Faculdade Jaguariaíva"},
            {"name": "FATEB - Faculdade de Telêmaco Borba"},
            {"name": "FANP - Faculdade do Noroeste Paranaense"},
            {"name": "FASBAM - Faculdade São Basílio Magno"},
            {"name": "FEITEP - Faculdade de Engenharia e Inovação Técnico Profissional"},
            {"name": "FG - Faculdade Guarapuava"},
            {"name": "FML - Faculdade Metropolitana Londrinense"},
            {"name": "UNICAMPO - Faculdade União de Campo Mourão"},
            {"name": "INTEGRADO - Centro Universitário Integrado de Campo Mourão"},
            {"name": "UniCesumar - Centro Universitário de Maringá"},
            {"name": "UNICURITIBA - Centro Universitário Curitiba"},
            {"name": "UNINTER - Grupo Educacional Uninter"},
            {"name": "UNIPAR - Universidade Paranaense"},
            {"name": "UNOPAR - Universidade do Norte do Paraná"},
            {"name": "UCP - Faculdades do Centro do Paraná"},
            {"name": "UP - Universidade Positivo"},
            {"name": "UTP - Universidade Tuiuti do Paraná"},
            {"name": "UNISEP - União de Ensino do Sudoeste do Paraná"},
            {"name": "UFPI - Universidade Federal do Piauí"},
            {"name": "IFPI - Instituto Federal do Piauí"},
            {"name": "UFDPar - Universidade Federal do Delta do Parnaíba"},
            {"name": "UESPI - Universidade Estadual do Piauí"},
            {"name": "ICESPI - Instituto Católico de Estudos de Ensino Superior do Piauí"},
            {"name": "UNINOVAFAPI - Centro Universitário Uninovafapi"},
            {"name": "UNINASSAU - Centro Universitário Maurício de Nassau"},
            {"name": "FeMASS - Faculdade Professor Miguel Ângelo da Silva Santos - Macaé"},
            {"name": "ISERJ - Instituto Superior de Educação do Rio de Janeiro"},
            {"name": "FAETERJ - Faculdade de Educação Tecnológica do Estado do Rio de Janeiro"},
            {"name": "UENF - Universidade Estadual do Norte Fluminense"},
            {"name": "UERJ - Universidade do Estado do Rio de Janeiro"},
            {"name": "UEZO - Universidade Estadual da Zona Oeste"},
            {"name": "IMPA - Instituto de Matemática Pura e Aplicada"},
            {"name": "CBPF - Centro Brasileiro de Pesquisas Físicas"},
            {"name": "CEFET/RJ - Centro Federal de Educação Tecnológica Celso Suckow da Fonseca"},
            {"name": "Colégio Pedro II - Colégio Pedro II"},
            {"name": "ENCE - Escola Nacional de Ciências Estatísticas"},
            {"name": "IFF - Instituto Federal Fluminense"},
            {"name": "IFRJ - Instituto Federal do Rio de Janeiro"},
            {"name": "UFF - Universidade Federal Fluminense"},
            {"name": "UFRJ - Universidade Federal do Rio de Janeiro"},
            {"name": "UFRRJ - Universidade Federal Rural do Rio de Janeiro"},
            {"name": "UNIRIO - Universidade Federal do Estado do Rio de Janeiro"},
            {"name": "ABMDP II - Academia de Bombeiro Militar Dom Pedro II"},
            {"name": "AMAN - Academia Militar de Agulhas Negras"},
            {"name": "APMDJ VI - Academia de Polícia Militar Dom João VI"},
            {"name": "EN - Escola Naval"},
            {"name": "ECEME - Escola de Comando e Estado-Maior do Exército"},
            {"name": "EsAO - Escola de Aperfeiçoamento de Oficiais"},
            {"name": "IME - Instituto Militar de Engenharia"},
            {"name": "ESPM-RIO - Escola Superior de Propaganda e Marketing"},
            {"name": "CELSO LISBOA - Centro Universitário Celso Lisboa"},
            {"name": "FACHA - Faculdades Integradas Hélio Alonso"},
            {"name": "FGV - Fundação Getulio Vargas"},
            {"name": "FMC - Faculdade de Medicina de Campos"},
            {"name": "FMP/FASE - Faculdade de Medicina de Petrópolis - Faculdade Arthur Sá Earp Neto"},
            {"name": "FSMA - Faculdade Salesiana de Macaé"},
            {"name": "FSB/RJ - Faculdade de São Bento do Rio de Janeiro"},
            {"name": "FUNENSEG - Escola Nacional de Seguros"},
            {"name": "IBMEC - Instituto Brasileiro de Mercado e Capitais"},
            {"name": "IBMR - Centro Universitário IBMR"},
            {"name": "MACKENZIE-RIO - Faculdade Presbiteriana Mackenzie Rio"},
            {"name": "PUC-RIO - Pontifícia Universidade Católica do Rio de Janeiro"},
            {"name": "UCAM - Universidade Cândido Mendes"},
            {"name": "UCB - Universidade Castelo Branco"},
            {"name": "UCP - Universidade Católica de Petrópolis"},
            {"name": "UGB - Centro Universitário Geraldo Di Biase"},
            {"name": "UNIFAA - Centro de Ensino Superior de Valença"},
            {"name": "UNISUAM - Centro Universitário Augusto Motta"},
            {"name": "UNIABEU - UNIABEU Centro Universitário"},
            {"name": "UNIFESO - Centro Universitário Serra dos Órgãos"},
            {"name": "UNIGRANRIO - Universidade do Grande Rio"},
            {"name": "UNIVERSO - Universidade Salgado de Oliveira"},
            {"name": "USS - Universidade Severino Sombra"},
            {"name": "USU - Universidade Santa Úrsula"},
            {"name": "UVA - Universidade Veiga de Almeida"},
            {"name": "AEDB - Faculdades Dom Bosco"},
            {"name": "SENAC - Faculdade Senac Rio de Janeiro"},
            {"name": "UBM - Centro Universitário de Barra Mansa"},
            {"name": "UNESA - Universidade Estácio de Sá"},
            {"name": "UNIFOA - Centro Universitário de Volta Redonda"},
            {"name": "UERN - Universidade do Estado do Rio Grande do Norte"},
            {"name": "IFRN - Instituto Federal do Rio Grande do Norte"},
            {"name": "UFERSA - Universidade Federal Rural do Semi-Árido"},
            {"name": "UFRN - Universidade Federal do Rio Grande do Norte"},
            {"name": "ULBRA - Universidade Luterana do Brasil (Polo Natal)"},
            {"name": "UNP - Universidade Potiguar"},
            {"name": "Fatern Gama Filho - Faculdade de Excelência do Rio Grande do Norte"},
            {"name": "UNOPAR - Universidade Norte do Paraná (Polo Natal)"},
            {"name": "UNINASSAU - Faculdade Maurício de Nassau - (Pólo Natal)"},
            {"name": "IPOG - Instituto de Pós-Graduação (Pólo Natal)"},
            {"name": "UERGS - Universidade Estadual do Rio Grande do Sul"},
            {"name": "FURG - Universidade Federal do Rio Grande"},
            {"name": "IFFarroupilha - Instituto Federal Farroupilha"},
            {"name": "IFRS - Instituto Federal do Rio Grande do Sul"},
            {"name": "IFSul - Instituto Federal Sul-rio-grandense"},
            {"name": "UFCSPA - Universidade Federal de Ciências da Saúde de Porto Alegre"},
            {"name": "UFPEL - Universidade Federal de Pelotas"},
            {"name": "UFRGS - Universidade Federal do Rio Grande do Sul"},
            {"name": "UFSM - Universidade Federal de Santa Maria"},
            {"name": "UNIPAMPA - Universidade Federal do Pampa"},
            {"name": "UFFS - Universidade Federal da Fronteira Sul"},
            {"name": "FACCAT - Faculdades de Taquara"},
            {"name": "FAPA - Faculdade Porto-Alegrense"},
            {"name": "FEEVALE - Universidade Feevale"},
            {"name": "PUCRS - Pontifícia Universidade Católica do Rio Grande do Sul"},
            {"name": "UCPEL - Universidade Católica de Pelotas"},
            {"name": "UCS - Universidade de Caxias do Sul"},
            {"name": "ULBRA - Universidade Luterana do Brasil"},
            {"name": "UNICRUZ - Universidade de Cruz Alta"},
            {"name": "UFN - Universidade Franciscana"},
            {"name": "UNIJUÍ - Universidade Regional do Noroeste do Estado do Rio Grande do Sul"},
            {"name": "UNIRITTER - Centro Universitário Ritter dos Reis"},
            {"name": "UNILASALLE-RJ - Universidade La Salle"},
            {"name": "UNISC - Universidade de Santa Cruz do Sul"},
            {"name": "UNISINOS - Universidade do Vale do Rio dos Sinos"},
            {"name": "UNIVATES - Universidade do Vale do Taquari"},
            {"name": "UPF - Universidade de Passo Fundo"},
            {"name": "URCAMP - Universidade da Região da Campanha"},
            {"name": "URI - Universidade Regional Integrada do Alto Uruguai e das Missões"},
            {"name": "ESMARGS - Escola Superior de Música e Artes do Rio Grande do Sul"},
            {"name": "ESPM - Escola Superior de Propaganda e Marketing"},
            {"name": "ESTEF - Escola Superior de Teologia e Espiritualidade Franciscana"},
            {"name": "Faculdade SOGIPA"},
            {"name": "FAACS - Faculdade Anglo-Americano de Caxias do Sul"},
            {"name": "FADERGS - Faculdade de Desenvolvimento do Rio Grande do Sul"},
            {"name": "FSG - Faculdade da Serra Gaúcha"},
            {"name": "IDEAU - Instituto de Desenvolvimento Educacional do Alto Uruguai (Getúlio Vargas)"},
            {"name": "SENAC - Faculdade do Serviço Nacional de Aprendizagem Comercial"},
            {"name": "SJT - Faculdades Integradas São Judas Tadeu"},
            {"name": "SLMANDIC - Faculdade de Odontologia São Leopoldo Mandic"},
            {"name": "UNIRITTER - Centro Universitário Ritter dos Reis"},
            {"name": "UNIR - Universidade Federal de Rondônia"},
            {"name": "IFRO - Instituto Federal de Rondônia"},
            {"name": "FCR - Faculdade Católica de Rondônia"},
            {"name": "UNIFSL - Centro Universitário São Lucas de Porto Velho"},
            {"name": "UNIFSL - Centro Universitário São Lucas de Ji-paraná"},
            {"name": "FAMA - Faculdade da Amazônia"},
            {"name": "UERR - Universidade Estadual de Roraima"},
            {"name": "UFRR - Universidade Federal de Roraima"},
            {"name": "IFRR - Instituto Federal de Roraima"},
            {"name": "FARES - Faculdade Roraimense de Ensino Superior"},
            {"name": "FURB - Fundação Universidade Regional de Blumenau"},
            {"name": "SOCIESC - Sociedade Educacional de Santa Catarina"},
            {"name": "UNESC - Universidade do Extremo Sul Catarinense"},
            {"name": "FMP - Faculdade Municipal de Palhoça"},
            {"name": "CEETEPS - Centro Estadual de Educação Tecnológica Paula Souza"},
            {"name": "UDESC - Universidade do Estado de Santa Catarina"},
            {"name": "UFFS - Universidade Federal da Fronteira Sul"},
            {"name": "IFSC - Instituto Federal de Santa Catarina"},
            {"name": "IFC - Instituto Federal Catarinense"},
            {"name": "UFSC - Universidade Federal de Santa Catarina"},
            {"name": "SENAC - Faculdade Senac - Santa Catarina"},
            {"name": "UNOESC - Universidade do Oeste de Santa Catarina"},
            {"name": "UNIASSELVI - Centro Universitário Leonardo da Vinci"},
            {"name": "UNISUL - Universidade do Sul de Santa Catarina"},
            {"name": "UNC - Universidade do Contestado"},
            {"name": "UNIARP - Universidade Alto Vale do Rio do Peixe"},
            {"name": "UNERJ - Centro Universitário de Jaraguá do Sul"},
            {"name": "UNIVALI - Universidade do Vale do Itajaí"},
            {"name": "UNIVILLE - Universidade da Região de Joinville"},
            {"name": "UNOCHAPECÓ - Universidade Comunitária Regional de Chapecó"},
            {"name": "UNIPLAC - Universidade do Planalto Catarinense"},
            {"name": "UNISUL - Universidade do Sul de Santa Catarina"},
            {"name": "Católica SC - Centro Universitário Católica de Santa Catarina"},
            {"name": "UNIAVAN - Centro Universitário Avantis"},
            {"name": "Cesusc - Complexo de Ensino Superior de Santa Catarina"},
            {"name": "Reitoria da Universidade de Taubaté (UNITAU)"},
            {"name": "UNITAU - Universidade de Taubaté"},
            {"name": "USCS - Universidade Municipal de São Caetano do Sul"},
            {"name": "Uni-FACEF - Centro Universitário Municipal de Franca"},
            {"name": "UNIFAE - Centro Universitário das Faculdades Associadas de Ensino"},
            {"name": "Uni-FACEF - Centro Universitário de Franca"},
            {"name": "CUFSA - Centro Universitário Fundação Santo André"},
            {"name": "FACCAMP - Faculdade de Campo Limpo Paulista"},
            {"name": "EEP/FUMEP - Escola de Engenharia de Piracicaba"},
            {"name": "FDF - Faculdade de Direito de Franca"},
            {"name": "FDSBC - Faculdade de Direito de São Bernardo do Campo"},
            {"name": "FMABC - Faculdade de Medicina do ABC"},
            {"name": "FMJ - Faculdade de Medicina de Jundiaí"},
            {"name": "FAI - Faculdades Adamantinenses Integradas"},
            {"name": "IMESA - Instituto Municipal de Ensino Superior de Assis"},
            {"name": "FEA - Fundação Educacional Araçatuba"},
            {"name": "USP - Universidade de São Paulo"},
            {"name": "UNICAMP - Universidade Estadual de Campinas"},
            {"name": "UNESP - Universidade Estadual Paulista"},
            {"name": "UNIVESP - Universidade Virtual do Estado de São Paulo"},
            {"name": "FAMEMA - Faculdade de Medicina de Marília"},
            {"name": "FAMERP - Faculdade de Medicina de São José do Rio Preto"},
            {"name": "FATEC - Faculdade de Tecnologia do Estado de São Paulo"},
            {"name": "APMBB - Academia de Polícia Militar do Barro Branco"},
            {"name": "UFSCar - Universidade Federal de São Carlos"},
            {"name": "UNIFESP - Universidade Federal de São Paulo"},
            {"name": "UFABC - Universidade Federal do ABC"},
            {"name": "INPE - Instituto Nacional de Pesquisas Espaciais"},
            {"name": "IFSP - Instituto Federal de Educação, Ciência e Tecnologia de São Paulo"},
            {"name": "Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) Campus Sertãozinho"},
            {"name": "ITA - Instituto Tecnológico de Aeronáutica"},
            {"name": "AFA - Academia da Força Aérea"},
            {"name": "PUC-SP - Pontifícia Universidade Católica de São Paulo"},
            {"name": "PUC-Campinas - Pontifícia Universidade Católica de Campinas"},
            {"name": "UNIARA - Universidade de Araraquara"},
            {"name": "UNISA - Universidade de Santo Amaro"},
            {"name": "UNISANTOS - Universidade Católica de Santos"},
            {"name": "UNIVAP - Universidade do Vale do Paraíba"},
            {"name": "UNOESTE - Universidade do Oeste Paulista"},
            {"name": "USF - Universidade São Francisco"},
            {"name": "UNISANT'ANNA - Universidade Sant'Anna"},
            {"name": "UMESP - Universidade Metodista de São Paulo"},
            {"name": "UNAERP - Universidade de Ribeirão Preto"},
            {"name": "MACK - Universidade Presbiteriana Mackenzie"},
            {"name": "UNIMEP - Universidade Metodista de Piracicaba"},
            {"name": "UNICASTELO - Universidade Camilo Castelo Branco"},
            {"name": "UNISAGRADO - Universidade do Sagrado Coração"},
            {"name": "UNISAL - Centro Universitário Salesiano de São Paulo"},
            {"name": "UNICID - Universidade Cidade de São Paulo"},
            {"name": "CUSC - Centro Universitário São Camilo"},
            {"name": "FEBASP - Centro Universitário Belas Artes de São Paulo"},
            {"name": "FEI - Centro Universitário FEI"},
            {"name": "UNIFEV - Centro Universitário de Votuporanga"},
            {"name": "FMU - Centro Universitário das Faculdades Metropolitanas Unidas"},
            {"name": "SENAC - Centro Universitário Senac"},
            {"name": "UNASP - Centro Universitário Adventista de São Paulo"},
            {"name": "UNICEP - Centro Universitário Central Paulista"},
            {"name": "UNIFAI - Centro Universitário Assunção"},
            {"name": "UNIFEB - Centro Universitário da Fundação Educacional de Barretos"},
            {"name": "UNIFEOB - Centro Universitário Octávio Bastos"},
            {"name": "UNIFIEO - Centro Universitário FIEO"},
            {"name": "UNILAGO - União das Faculdades dos Grandes Lagos"},
            {"name": "UNIMONTE - Centro Universitário Monte Serrat"},
            {"name": "UNIVEM - Centro Universitário Eurípedes de Marília"},
            {"name": "ACCC - A.C.Camargo Cancer Center"},
            {"name": "FCN - Faculdade Canção Nova"},
            {"name": "BSP - Business School São Paulo"},
            {"name": "FGV - Fundação Getúlio Vargas"},
            {"name": "FECAP - Fundação Escola de Comércio Álvares Penteado"},
            {"name": "ESPM - Escola Superior de Propaganda e Marketing"},
            {"name": "ESAGS - Escola Superior de Administração e Gestão"},
            {"name": "IMT - Instituto Mauá de Tecnologia"},
            {"name": "FCL - Faculdade Cásper Líbero"},
            {"name": "FAAP - Fundação Armando Álvares Penteado"},
            {"name": "FACERES - Faculdade Ceres de Medicina"},
            {"name": "Insper - Instituto de Ensino e Pesquisa"},
            {"name": "IMT - Instituto Mauá de Tecnologia"},
            {"name": "FESPSP - Fundação Escola de Sociologia e Política de São Paulo"},
            {"name": "FRB - Faculdades Integradas Rio Branco"},
            {"name": "FIO - Faculdades Integradas de Ourinhos"},
            {"name": "FIRB - Faculdades Integradas Rio Branco"},
            {"name": "FTML - Faculdade de Teologia Metodista Livre"},
            {"name": "FAZP - Faculdade Zumbi dos Palmares"},
            {"name": "FCMSCSP - Faculdade de Ciências Médicas da Santa Casa de São Paulo"},
            {"name": "FDC - Fundação Dom Cabral"},
            {"name": "FASM - Faculdade Santa Marcelina"},
            {"name": "UNINOVE - Campus Memorial - São Paulo/SP"},
            {"name": "ICESP - Universidade Brasil"},
            {"name": "ISES - Centro Universitário Sumaré"},
            {"name": "ITE - Centro Universitário de Bauru"},
            {"name": "UAM - Universidade Anhembi Morumbi"},
            {"name": "UBC - Universidade Braz Cubas"},
            {"name": "UMC - Universidade de Mogi das Cruzes"},
            {"name": "UNG - Universidade Guarulhos"},
            {"name": "UniABC - Universidade do Grande ABC"},
            {"name": "UNIBAN - Universidade Bandeirante de São Paulo"},
            {"name": "UNICSUL - Universidade Cruzeiro do Sul"},
            {"name": "UNIFRAN - Universidade de Franca"},
            {"name": "UNIMAR - Universidade de Marília"},
            {"name": "UNINOVE - Universidade Nove de Julho"},
            {"name": "UNIP - Universidade Paulista"},
            {"name": "UNIMES - Universidade Metropolitana de Santos"},
            {"name": "UNISANTA - Universidade Santa Cecília"},
            {"name": "UNISO - Universidade de Sorocaba"},
            {"name": "USJT - Universidade São Judas Tadeu"},
            {"name": "UNITOLEDO - Centro Universitário Toledo"},
            {"name": "FACAMP - Faculdades de Campinas"},
            {"name": "FADI - Faculdade de Direito de Sorocaba"},
            {"name": "FADISC - Faculdades Integradas de São Carlos"},
            {"name": "FAM - Faculdade de Americana"},
            {"name": "FIAP - Faculdade de Informática e Administração Paulista"},
            {"name": "FADITU - Faculdade de Direito de Itu"},
            {"name": "FIRB - Faculdades Integradas Rio Branco"},
            {"name": "FIT - Faculdade Impacta Tecnologia"},
            {"name": "FOC - Faculdades Oswaldo Cruz"},
            {"name": "SLMANDIC - Faculdade de Odontologia e Centro de Pesquisas Odontológicas São Leopoldo Mandic"},
            {"name": "ESEG - Escola Superior de Engenharia e Gestão"},
            {"name": "UFS - Universidade Federal de Sergipe"},
            {"name": "IFS - Instituto Federal de Sergipe"},
            {"name": "Unit - Universidade Tiradentes"},
            {"name": "FPD - Faculdade Pio Décimo"},
            {"name": "ESTÁCIO - Faculdade Estácio de Sergipe"},
            {"name": "FANESE - Faculdade de Administração e Negócios de Sergipe"},
            {"name": "FAMA - Faculdade Amadeus"},
            {"name": "FSLF - Faculdade São Luis de França"},
            {"name": "UNOPAR - Universidade Norte do Paraná"},
            {"name": "FASER - Faculdade Sergipana"},
            {"name": "FACAR - Faculdade de Aracaju"},
            {"name": "UNIRB - Faculdade Serigy"},
            {"name": "FAJAR - Faculdade Jardins"},
            {"name": "FA - Faculdade Atlântico"},
            {"name": "UniCOC - Sistema COC de Educação"},
            {"name": "UNINASSAU - Faculdade Maurício de Nassau"},
            {"name": "UnirG - Universidade de Gurupi"},
            {"name": "UNITINS - Universidade Estadual do Tocantins"},
            {"name": "IFTO - Instituto Federal do Tocantins"},
            {"name": "UFT - Universidade Federal do Tocantins"},
            {"name": "UNICATÓLICA - Centro Universitário Católica do Tocantins"},
            {"name": "FACDO - Faculdade Católica Dom Orione"},
            {"name": "CEULP/ULBRA - Centro Universitário Luterano de Palmas"},
        ]

        for university in universities:
            University.objects.get_or_create(
                name=university["name"], defaults={"description": ""})
            self.stdout.write(self.style.SUCCESS(
                f'University {university["name"]} added or already exists.'))
