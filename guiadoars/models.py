from django.db import models

# Tabela Topic no banco de dados



  class Meta:
    verbose_name_plural = 'entries' #Qnd o Django quiser usar o Entry no plural, muda a palavra p/ plural

  def __str__(self):
    """Devolve uma representacao em string do modelo."""
    return self.text[:50] + '...' #Mostra apenas os 50 primeiros caracteres
  
  from django.db import models

class Instituicao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    cidade = models.CharField(max_length=100)
    tipo_doacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
  