<html>
<body>
    <h2>Cloud Native Orchestration </h2>
<strong>Capstone project for Udacity's Cloud DevOps Engineer</strong><br/>
---
<h3>Description</h3>
This project consist to deploy a simple API into a cluster Kubernetes using deployment Blue/Green and Rolling techniques.<br/>
---
<h3>Setting Environment</h3>
It was used Jenkins to automate manage of the Cluster Kubernetes and Application on AWS EC2 Instance based on Ubuntu 18.04 image. <br/><br/>
<strong>Requirements:</strong>
<ul>
  <li>
    Java
    <ul>
      <li><code>$ sudo apt-get update</code></li>
      <li><code>$ sudo apt install -y default-jdk</code></li>
    </ul>
  </li>
  <li>
    Jenkins
    <ul>  
      <li><code>$ wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -</code></li>
      <li><code>$ sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'</code></li>
      <li><code>$ sudo apt-get update</code></li>
      <li><code>$ sudo apt-get install jenkins</code></li>     
      <li><code>$ sudo systemctl start jenkins</code></li>
      <li><code>$ sudo systemctl enable jenkins</code></li>
      <li><code>$ sudo systemctl status jenkins</code></li>      
    </ul>
  </li>
  
  <li>
    Jenkins Plugins
    <ul>
      <li>Blue Ocean</li>
      <li>Pipeline: AWS Steps</li>
      <li>CloudBees AWS Credentials</li>      
    </ul>
  </li>
  
  <li>
    Pip for Python 3
    <ul>
      <li><code>$ sudo apt update</code></li>
      <li><code>$ sudo apt install python3-pip</code></li>
    </ul>  
  </li>  
  
  <li>
    AWS Client
    <ul>  
      <li><code>$ pip install awscli --upgrade --user</code></li>  
    </ul>
  </li>
  
  <li>
    EKSCTL
    <ul>
      <li><code>$ curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp</code></li>
      <li><code>$ sudo mv /tmp/eksctl /usr/local/bin</code></li>
    </ul>    
  </li>
  
  <li>
    AWS-IAM-Authenticator
    <ul>
      <li><code>$ curl -o aws-iam-authenticator https://amazon-eks.s3.us-west-2.amazonaws.com/1.15.10/2020-02-22/bin/linux/amd64/aws-iam-authenticator</code></li>
      <li><code>$ chmod +x ./aws-iam-authenticator</code></li>
      <li><code>$ sudo mv aws-iam-authenticator /usr/local/bin</code></li>      
    </ul>    
  </li>
  
  <li>
    Kubectl
    <ul>  
      <li><code>$ curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/linux/amd64/kubectl</code></li>
      <li><code>$ chmod +x ./kubectl</code></li>
      <li><code>$ sudo mv ./kubectl /usr/local/bin/kubectl</code></li>      
    </ul>
  </li>
</ul>
<br/>
<strong>AIM Role:</strong><br/>
Create a AIM Role with all policies EKS * and attach it on EC2 Instance. This way you don't need to configure your credentials on EC2 instance.

</body>
</html>
