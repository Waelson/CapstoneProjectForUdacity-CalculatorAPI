
<h2>Cloud Native Orchestration</h2>

<strong>Capstone project for Udacity's Cloud DevOps Engineer</strong><br/>

<h3>Description</h3>
This project consists of deploying an API in a Kubernetes Cluster using deployment Rolling technique.<br/> The application used in this project is based on Python and Flask. This project has a single endpoint:<br/><br/>
<ul>
  <li><strong>/api/v0/multiply</strong></li>
  <ul>
    <li>Usage: <code>http://localhost:5001/api/v0/multiply?param1=12&#38;param2=2</code></li>
  </ul>
</ul>

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
    Docker Engine
    <ul>      
      <li><code>$ sudo apt-get install docker-ce docker-ce-cli containerd.io</code></li> 
    </ul>
  
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
Create a AIM Role with all policies <i>AmazonEKS*</i> and attach it on EC2 Instance running Jenkins. This way you don't need to configure your credentials into EC2 instance.<br/>

<h3>Validating Environment</h3>
1 - Connect to EC2 instance and run command below to create a cluster. This command can to take about 15 minutos to finish.<br/>
<code>$ eksctl create cluster --name &#60;cluster-name&#62; --region &#60;region&#62; --nodegroup-name standard-workers --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --managed</code><br/><br/>
2 - Next, we need to update a <code>˜/.kube/config</code>.<br/>
<code>$ aws eks update-kubeconfig --name &#60;cluster-name&#62;</code><br/><br/>
3 - Now, we let's get information of the cluster using <code>kubectl</code>.<br/>
<code>$ kubectl cluster-info</code><br/><br/>
4 - Finally, delete cluster.<br/>
<code>$ eksctl delete cluster cluster --name &#60;cluster-name&#62; --region &#60;region&#62;</code
