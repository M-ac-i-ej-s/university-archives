import Keycloak from "keycloak-js";
const keycloak = new Keycloak({
 url: "http://localhost:8080/",
 realm: "myRealm",
 clientId: "React-auth",
});

export default keycloak;