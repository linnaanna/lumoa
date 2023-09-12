SELECT propertydata.id, propertydata.location, propertydata.code,
    eldata.tammi1,
    eldata.tammi2,
    eldata.tammi3,
    eldata.tammi4,
    eldata.tammi5,
    eldata.tammi6,
    eldata.tammi7,
    eldata.tammi8,
    eldata.tammi9,
    eldata.tammi10,
    eldata.tammi11,
    eldata.tammi12,
    eldata.tammi13,
    eldata.tammi14
FROM propertydata INNER JOIN eldata
ON propertydata.code = eldata.id

Yhdistin taulut inner joinilla käyttäen property codea ja id:tä, jolloin yhdistettyyn 
tauluun tulee selvyyden vuoksi tietoja taulusta propertydata vain sellaisista kiinteistöistä, 
joiden sähkönkäyttö löytyy taulusta eldata.