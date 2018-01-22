#!groovy
node {
  stage("Code Checkout") {
    checkout([$class: 'GitSCM', branches: [[name: "*/master"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: "Sandeep_GITHUB", url: "https://github.com/awscodedeploy/drone.git"]]])
  }
  stage("code commit") {
    sh "touch README.md"
    sh "git commit -am "touched README.md file"
    sh "git push origin master"
  }
}
