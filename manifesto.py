class manifestoGENAI:
    """
    Classe altamente coesa responsável por armazenar e exibir
    os princípios de comunicação e uso de IAs Generativas.
    """

    principios = ("""
        1. Todo prompt deve ser melhorado a qualquer momento.\n
        2. Entenda que o óbvio também precisa ser dito.\n
        3. Nem todas as experiências são individuais.\n
        4. Humanize as IAs generativas com seu repertório de vida.\n
        5. A novidade de hoje nem sempre é útil de fato.\n
        6. Contexto é o que alimenta a comunicação com IAs generativas.\n
        7. A teoria é incrível, mas aplique isso em projetos práticos.\n
        8. Lembre-se de documentar seus resultados.\n
        9. Melhor decompor o problema em partes menores.\n
        10. A simplicidade pode ser a solução em muitas situações.\n
        11. Encontre a documentação oficial do que quer aprender.\n
        12. Estruturar o formato de saída é um exercício de consistência.\n
        13. Sem ansiedade para não gastar tempo e dinheiro.\n
        14. Tenha foco no que quer comunicar, e não em detalhes.\n
        15. Utilize a IA generativa como ferramenta de cocriação.\n
        16. Diversifique as IAs generativas para evitar dependência.\n
        17. Enfatize o que é inegociável e crie regras explícitas.\n
        18. Saiba que a responsabilidade é nossa ao gerar algo com IA.\n
        19. Erros são oportunidades de recalcular a rota.\n
        20. Mantenha a criatividade contigo e delegue o que é chato.\n
        21. Prompt estruturado ajuda muito no entendimento.\n
        22. Revise os resultados gerados por IA generativa.\n
        23. Exemplos são bons para mostrar o que quer.
        """
    )

    def __init__(self):
        """
        Ao instanciar a classe, o easter egg é revelado no console,
        semelhante ao comportamento do clássico 'import this' do Python.
        """
        self.lista()

    def lista(self) -> None:
        """
        Exibe o conteúdo estruturado em formato de lista.
        """
        # Centralizando o título em 80 caracteres
        titulo = "TENHA CALMA E ESTUDE SEMPRE"
        subtitulo = "Um manifesto sobre boas práticas de uso da IA generativa"
        autor = "Autor: Mário Lúcio"


        print(titulo.center(80))
        print(subtitulo.center(85))
        print("\n")
        print(self.principios)
        print("\n")
        print(autor.center(33))
