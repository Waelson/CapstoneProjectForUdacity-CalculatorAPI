
<h2>Cloud Native Orchestration</h2>

<strong>Capstone project for Udacity's Cloud DevOps Engineer</strong><br/>

<h3>Description</h3>
This project consists of deploying an API in a Kubernetes Cluster using deployment Rolling Update technique.<br/> The application used in this project is based on Python and Flask. This project has a single endpoint:<br/><br/>
<ul>
  <li><strong>/api/v0/multiply</strong></li>
  <ul>
    <li>Usage: <code>http://localhost:5001/api/v0/multiply?param1=12&#38;param2=2</code></li>
  </ul>
</ul>

<h3>Content of Repository</h3>
<ul>
  <li>scripts</li>
  <li>descriptors-k8s</li>
  <li>images</li>
</ul>

<h3>Setting Environment CI/CD</h3>
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
<strong>Tip - Use AIM Role:</strong><br/>
Create a AIM Role with all policies <i>AmazonEKS*</i> and attach it on EC2 Instance running Jenkins. This way you don't need to configure your credentials into EC2 instance.<br/>

<h3>Validating Environment</h3>
1 - Connect to EC2 instance and execute the command below to create a cluster with 3 nodes. This command can to take about 15 minutes to finish. Be patient!<br/>
<code>$ eksctl create cluster --name &#60;cluster-name&#62; --region &#60;region&#62; --nodegroup-name standard-workers --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --managed</code><br/><br/>
2 - Next, we need to update <code>˜/.kube/config</code> file, so that you can use the <code>kubectl</code> command.<br/>
<code>$ aws eks update-kubeconfig --name &#60;cluster-name&#62;</code><br/><br/>
3 - Now, we let's get information of the cluster using <code>kubectl</code> command.<br/>
<code>$ kubectl cluster-info</code><br/><br/>
4 - Finally, delete cluster.<br/>
<code>$ eksctl delete cluster cluster --name &#60;cluster-name&#62; --region &#60;region&#62;</code>

<h3>Rolling Update Release</h3>
As defined by the website kubernetes.io, rolling updates is a strategy that allow you deployments' update to take place with zero downtime by incrementally updating Pods instances with new ones. 
<br/>
Below snnipet code from the file `deployment.yaml` used in this project to deploy application.<br/><br/>

```
...
spec:
  replicas: 2
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 50%
      maxSurge: 1
...
```

<h3>More Informations</h3>
<ul>
  <li>Getting started with EKSCTL - <a href="https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html">https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html</a></li>
  <li>Launch a guest book application - <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-guestbook.html">https://docs.aws.amazon.com/eks/latest/userguide/eks-guestbook.html</a></li>
  <li>Create a SSH Key - <a href="https://eksworkshop.com/prerequisites/sshkey.html">https://eksworkshop.com/prerequisites/sshkey.html</a></li>  
  <li>Install Jenkins on Ubuntu - <a href="https://wiki.jenkins.io/display/JENKINS/Installing+Jenkins+on+Ubuntu">https://wiki.jenkins.io/display/JENKINS/Installing+Jenkins+on+Ubuntu</a></li>
  <li>How to Install Pip on Ubuntu 18.04 - <a href="https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/">https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/</a></li>  
  <li>Install Docker Engine on Ubuntu - <a href="https://docs.docker.com/engine/install/ubuntu/">https://docs.docker.com/engine/install/ubuntu/</a></li>
  <li>Installing aws-iam-authenticator - <a href="https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html">https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html</a></li>
  <li>Install and Set Up kubectl - <a href="https://kubernetes.io/docs/tasks/tools/install-kubectl/">https://kubernetes.io/docs/tasks/tools/install-kubectl/</a></li>  
</ul>
