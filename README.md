# GrowLyst
A Cannabis Grow Diary (can be used for other Plants as well)


Bootstrap: https://django-bootstrap-v5.readthedocs.io/en/latest/quickstart.html

## TODOs

- implement custom user action-types, nutrients, ...

## How it works

### Plants

### Grow

A grow is not required but can be used to group plants across different environments. (e.g. put clones from phenos in a tent parallel to the phenos you grow out).

### Group

A group is a optional subcategory for a grow. (e.g. you could divide the plants in a grow into the plants you grow and the clones even if you grow your plants in two different environments)

### Environment

An environment is required to create a plant. A plant cannot be created without an environment. An environment can be used to store multiple plants and to group them. You can also perform actions or measurements on the environment which apply to all plants inside of it (e.g. Adjusting the lights). 