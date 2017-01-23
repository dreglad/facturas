# Facturas

## Requerimientos
La versión *más reciente* de:
 - [Virtualbox][1]
 - [Vagrant][2]

## Instalación
  1. Clonar repositorio
  ```{r, engine='bash'}
  $ git clone https://github.com/dreglad/facturas
  $ cd facturas
  ```

  1. Iniciar el ambiente:
  ```{r, engine='bash'}
  $ vagrant up
  ```

## Uso
  - Backend: http://10.0.15.10/admin/ (u/p: admin/papanicolau)
  - Servidor de correo: 10.0.15.10 puerto 25
  - API REST: http://10.0.15.10/api/

  [1]: https://www.virtualbox.org/ "Oracle Virtualbox"
  [2]: https://www.vagrantup.com/ "Vagrant"
