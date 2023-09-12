SELECT propertydata.id,
propertydata.location,
propertydata.code,
eldatata.tammi1,
eldatata.tammi2,
eldatata.tammi3,
eldatata.tammi4,
eldatata.tammi5,
eldatata.tammi6,
eldatata.tammi7,
eldatata.tammi8,
eldatata.tammi9,
eldatata.tammi10,
eldatata.tammi11,
eldatata.tammi12,
eldatata.tammi13,
eldatata.tammi14
FROM propertydata
INNER JOIN eldatata
ON propertydata.code = eldatata.id