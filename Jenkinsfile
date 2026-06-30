pipeline {
    agent any

    stages {
        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes integrados dentro do container com Node e Python...'
                
                script {
                    // Pull da nova imagem combinada
                    bat 'docker pull nikolaik/python-nodejs:python3.10-nodejs16-alpine'
                    
                    // Execução utilizando a imagem que já tem tudo pronto
                    bat '''
                        docker run --rm \
                        -v "%WORKSPACE%":/workspace \
                        -w /workspace \
                        nikolaik/python-nodejs:python3.10-nodejs16-alpine \
                        sh -c "node -v && python -v && python testes_main.py -v"
                    '''
                }
            }
        }
    }
}
//set "PATH=C:\\Users\\Lucas Rangel\\AppData\\Local\\Programs\\Python\\Python312;%PATH%"