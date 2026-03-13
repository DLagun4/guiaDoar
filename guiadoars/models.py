from django.db import models

# Tabela Topic no banco de dados
class Topic(models.Model):
  """Um assunto sobre o qual o usuario esta aprendendo."""
  text = models.CharField(max_length=200) #No maximo 200 caracteres
  date_added = models.DateTimeField(auto_now_add=True) #Registrar a data e hora junto com o text

  def __str__(self): #Aparecer no Painel Administrativo
    """Devolve uma representacao em string do modelo."""
    return self.text
  
class Entry(models.Model):
  """Algo especifico aprendido sobre um assunto."""
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #Para cada topico aqui, relaciona com um topico que existe
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'entries' #Qnd o Django quiser usar o Entry no plural, muda a palavra p/ plural

  def __str__(self):
    """Devolve uma representacao em string do modelo."""
    return self.text[:50] + '...' #Mostra apenas os 50 primeiros caracteres
  
  from django.db import models

class Instituicao(models.Model):
    TIPO_INSTITUICAO = [
        ('igreja', 'Igreja'),
        ('ong', 'ONG'),
        ('abrigo', 'Abrigo'),
        ('escola', 'Escola'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  # Ex: SP, RJ
    cep = models.CharField(max_length=9, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    site = models.URLField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_INSTITUICAO, default='ong')
    tipo_doacao = models.CharField(max_length=100)  # Pode virar um campo ManyToMany futuramente
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
  