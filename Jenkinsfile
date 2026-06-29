pipeline {
    agent {
        docker { image 'node:16-alpine' }
    }

    stages {
        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes integrados do repositório...'
                sh '''
                    python testes_main.py -v
                '''
            }
        }
    }
}

//set "PATH=C:\\Users\\Lucas Rangel\\AppData\\Local\\Programs\\Python\\Python312;%PATH%"