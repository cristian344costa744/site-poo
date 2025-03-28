from flask import Flask, render_template

app = Flask(__name__)

# Definindo a classe base abstrata
from abc import ABC, abstractmethod

class Animal(ABC):
    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def som(self):
        pass

# Definindo classes que herdam de Animal
class Cachorro(Animal):
    def som(self):
        return "Au Au!"

class Gato(Animal):
    def som(self):
        return "Miau!"

@app.route('/')
def index():
    # Exemplo de uso da abstração
    cachorro = Cachorro()
    gato = Gato()
    
    # Dados a serem passados para o template
    dados = {
        'animal_1': cachorro.som(),
        'animal_2': gato.som(),
        'explicacao': "A abstração em POO permite que você defina um método na classe base (Animal), mas a implementação real é feita nas subclasses (Cachorro, Gato)."
    }

    return render_template('abstracao.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)

