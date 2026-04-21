# Arkkitehtuurikuvaus

## Rakenne


![Luokkajapakkausrakenne](./kuvat/arkkitehtuuri-luokka-pakkauskaavio.png)


## Sovelluslogiikka

```mermaid
 classDiagram
      Movies "*" --> "1" User
      class User{
          username
          password
      }
      class Movies{
          id
          title
          year
          seen
          user
          stars
      }
```
