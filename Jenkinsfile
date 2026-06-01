pipeline {
    agent any

    stages {
        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes integrados do repositório...'
                bat 'python testes_main.py -v'
            }
        }
    }
}