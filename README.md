## Summary
- Forked over from airflow's tutorial, building out custom DAGs for brainstorming out ideas.
## Project Structure

- **dags/**: This directory is the heart of the Airflow operation, where I've scripted DAGs for various data tasks. Among these, the `example_astronauts` DAG is a neat little pipeline querying astronauts in space via the Open Notify API. To get a feel for Airflow, I highly recommend the [Getting Started Tutorial](https://docs.astronomer.io/learn/get-started-with-airflow) I used.

- **Dockerfile**: Contains the Astro Runtime Docker image setup for Airflow. It's tailored to my project's needs but is adaptable for future requirements.

- **include/**: Houses additional files that support my DAGs, making the whole system tick.

- **packages.txt**: A list of OS-level packages my project depends on. It's a simple file, but essential for the environment.

- **requirements.txt**: The Python dependencies needed to make the magic happen. This file is crucial for ensuring consistency across installations.

- **plugins/**: Airflow is great, but sometimes you need that extra oomph—this folder contains custom and community plugins that extend functionality.

- **airflow_settings.yaml**: Configuration is key in data engineering. This file helps me manage Airflow Connections, Variables, and Pools with ease.

## Running Locally

Running this setup on your machine involves a few steps:

1. **Starting Up**: `astro dev start` kicks everything off, spinning up containers for the Postgres metadata database, the Airflow webserver, the scheduler, and the triggerer.

2. **Verification**: A quick `docker ps` should show all 4 containers up and running. It's always a relief to see everything working as expected.

3. **Access**: The Airflow UI is available at `http://localhost:8080/`, with `admin/admin` as the trusty login. The Postgres database is accessible at `localhost:5432/postgres`, a gateway to the underlying data.

## Deploying to Astronomer

While I'm mainly running things locally, deploying to an Astronomer cloud instance is straightforward. Their [documentation](https://docs.astronomer.io/cloud/deploy-code/) has been a helpful guide.

## Contact

It's just me here, so feel free to reach out if you're interested in this project, have suggestions, or want to chat about data engineering! The Astronomer CLI has been a great asset, and I'm always open to learning more from the community.
