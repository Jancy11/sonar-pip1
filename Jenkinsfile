pipeline {
agent any
environment {
PYTHON_PATH =
&#39;C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\LENOVO\\AppDa
ta\\Local\\Programs\\Python\\Python313\\Scripts&#39;
}
stages {
stage(&#39;Checkout&#39;) {
steps {
checkout scm
}
}
stage(&#39;Build&#39;) {
steps {
// Set the PATH and install dependencies using pip
bat &#39;&#39;&#39;
set PATH=%PYTHON_PATH%;%PATH%
pip install -r requirements.txt
&#39;&#39;&#39;
}
}
stage(&#39;SonarQube Analysis&#39;) {
environment {
SONAR_TOKEN = credentials(&#39;sonarqube-token&#39;) // Accessing the SonarQube token stored
in Jenkins credentials
}
steps {
bat &#39;&#39;&#39;
set PATH=%PYTHON_PATH%;%PATH%

sonar-scanner -Dsonar.projectKey=github_trial1 \
-Dsonar.projectName=Trial1 \
-Dsonar.sources=. \
-Dsonar.host.url=http://localhost:9000 \
-Dsonar.token=%SONAR_TOKEN%
&#39;&#39;&#39;
}
}
}
post {
success {
echo &#39;Pipeline completed successfully&#39;
}
failure {
echo &#39;Pipeline failed&#39;
}
always {
echo &#39;This runs regardless of the result.&#39;
}
}
}
