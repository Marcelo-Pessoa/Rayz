pipeline {
    agent any

    stages {
        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes integrados do repositório...'
                bat '''
                    set "PATH=C:\\Users\\Lucas Rangel\\AppData\\Local\\Programs\\Python\\Python312;%PATH%"
                    dir
                    python test_main.py -v
                '''
            }
        }
    }
}