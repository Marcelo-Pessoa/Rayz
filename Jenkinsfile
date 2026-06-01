pipeline {
    agent any

    stages {
        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes integrados do repositório...'
                sh  'python3 testes_main.py -v'
            }
        }
    }
}