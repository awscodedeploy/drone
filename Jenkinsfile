#!groovy
node {
  stage("Code Checkout") {
    checkout([$class: 'GitSCM', branches: [[name: "*/master"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: "Sandeep_GITHUB", url: "https://github.com/awscodedeploy/drone.git"]]])
  }
}
