# structure

```
├── cluster
│   ├── ecr.tf
│   ├── eks.tf
│   ├── iam_policy.json
│   ├── main.tf
│   ├── node-groups.tf
│   ├── README.md
│   ├── remote-state.tf
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   └── vars.tf
├── iam_policy.json
└── readme.md
```

One needs to install following version of awscli and kubectl as well as terraform

| tool | version |  
| terraform | v1.4.2 |  
| aws | aws-cli/2.13.1 |  
| kubectl | v5.0.1 |


# install

```
terraform init
```

```
terraform apply
```