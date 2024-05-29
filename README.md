# bundle-examples

This repository provides Databricks Asset Bundles examples, with added CI/CD pipelines using Azure Devops

For more details, see the READMEs in each subfolder, e.g. [default_python README](./default_python/README.md)

To learn more, see:
* The public preview announcement at 
https://www.databricks.com/blog/announcing-public-preview-databricks-asset-bundles-apply-software-development-best-practices
* The docs at https://docs.databricks.com/dev-tools/bundles/index.html


## CI/CD Process flow:
![CI/CD Process Flow diagram](./Resources/ci_cd_process_flow.png)

[Source Diagram](https://docs.google.com/presentation/d/1GkZlCJDqqqaeZYFR60Df3uZkdkjIegQgQNAztBEInk8/edit?usp=sharing)

CI pipeline definitions are in: `default_python/azure_devops_pipelines/`

Description:
1. Engineer create a new branch using their IDE of choice, or the Databricks Repos UI
2. Engineer makes code changes, runs unit tests locally and integration tests against the dev workspace
3. Once the feature is complete, the engineer creates a Pull Request in Azure Devops Repos
4. Azure Devops Pipelines automatically triggers a run of the Pull Requests CI pipeline. This runs tests and deploys the Databricks Asset Bundle (DAB) to the development environment
5. Once all automated checks have been completed and pull request has been approved, the engineer completes the pull request to merge the code into the main branch
6. Azure Devops Pipelines automatically triggers a run of the Staging CI pipeline. This tests the code again, but against the Staging environment, which likely has more realistic production data and config. It deploys the DAB to the environment
7. (Optional) The engineer wants to release the code to the production environment, so creates a new Pull Request to merge all the code from the main branch into the release branch
8. Once the Pull Request has been reviewed, it is completed and the code is merged into the release branch
9. Azure Devopis Pipelines automatically triggers the Prod CI pipeline, deploying the DAB to production, this typically includes a scheduled trigger for the job to run at a given time


## Creating a service principle to use with CI process
1. Create a service principle in Azure Entra ID or in Databricks directly if you don't have SCIM set up. See https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/service-principals

Alternatively, you can use a personal access token from Databricks instead. Change the environment variables in the pipeline files and Azure Devops variable group appropriately. 

## Setting up environment specific variables/secrets
1. Go to Azure Pipelines
1. Click 'Library'
1. Create new variable group
1. Name it `dev-variable-group`
1. Add the following variables:
    - `BUNDLE_VAR_notifications_email_address` : Optional email address to use for failure notifications
    - `DATABRICKS_CLIENT_ID` : Service Principle client id used to authenticate with Databricks
    - `DATABRICKS_CLIENT_SECRET` : Service Principle secret use to authenticate with Databricks. Set this to secret to avoid it displaying in the UI
    - `DATABRICKS_CLUSTER_ID` : Used by DBConnect to run automated tests against Databricks interactive cluster
    - `DATABRICKS_HOST` : Databricks host used by CLI and tests, e.g. https://demo-workspace.cloud.databricks.com/
1. Clone this variable group for staging and prod, call these `staging-variable-group` and `prod-variable-group`. Change values accordingly. 

## Setting up Azure Pipelines
1. Go to Azure Pipelines
1. Click 'New Pipeline'
1. Select Azure Repos Git and then this Git repo
1. Select Existing Azure Pipelines YAML file
1. Select main branch and default_python/azure_devops_pipelines/azure_pipeline_pull_request.yml
1. Run pipeline
1. Repeat steps for the staging and production CI pipelines

