pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Obtendo o código fonte do repositório GitHub...'
                checkout scm
            }
        }

        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes armazenados no repositório...'
                
                bat '''
                    set "PATH=C:\\Users\\Lucas Rangel\\AppData\\Local\\Programs\\Python\\Python312;%PATH%"
                    python test_main.py -v
                '''
            }
        }
    }
}