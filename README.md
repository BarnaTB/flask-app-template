# Recommend Staffs for Client and Internal Projects based on Skills and Expertise

## Documentation, Setup, and Usage Instructions

Before you setup the project, please make sure you have installed `docker`, `docker compose` and `Make` installed according to the following OS specific instructions.

> ### Windows Make, Docker, Docker Compose Installation Instructions

- To install Make, [click this link](https://thrivemyway.com/how-to-install-and-use-make-in-windows/).
- To install Docker and Docker Compose, [click this link](https://docs.docker.com/desktop/install/windows-install/).
- With these two installations you should be ready to move on the `Setup` section of this documentation.

> ### Ubuntu Make, Docker, Docker Compose Installation Instructions

- To install Make, [click this link](https://linuxhint.com/run-makefile-windows/).
- To install Docker and Docker Compose, [click this link](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-install-Docker-and-docker-compose-on-Ubuntu).
- With these two installations you should be ready to move on the `Setup` section of this documentation.

## Setup

- Make sure the latest version of docker and docker compose.
- CD into project root and run ```make build``` to setup the project.
- Create a `.env` file.
- Copy the contents of the `.env.example` file and paste them in the `.env` file. Reach out to the developer team for specific values to use.
- Run ```make up``` to start the application.

## What It Does

This flask api service recommends staff for client and internal projects based on staff's expertise level, skills and other parameters

Visit http://127.0.0.1:5000/api and you should see
```json
{
    "response": "Welcome to Staff Recommender API Service!"
}
```

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) for details.

### Testing

``` bash
 python -m pytest tests\
```

### Security

If you discover any security-related issues, please use the issue tracker.

## Credits

- [Emmanuel Jean Kamasah](https://github.com/emmajeankamasah)
- [Barnabas Tumuhairwe](https://github.com/BarnaTB)
- [All Contributors](contributors.md)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
