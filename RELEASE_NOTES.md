# API Changelog 2.56 vs. 2.57

## GET /active-directory
-  added the optional property 'items/ca_certificate' to the response with the '200' status
-  added the optional property 'items/ca_certificate' to the response with the '207' status
-  added the optional property 'items/ca_certificate_group' to the response with the '200' status
-  added the optional property 'items/ca_certificate_group' to the response with the '207' status


## PATCH /active-directory
-  added the new optional request property 'ca_certificate'
-  added the new optional request property 'ca_certificate_group'
-  added the optional property 'items/ca_certificate' to the response with the '200' status
-  added the optional property 'items/ca_certificate_group' to the response with the '200' status


## POST /active-directory
-  added the new optional request property 'ca_certificate'
-  added the new optional request property 'ca_certificate_group'
-  added the optional property 'items/ca_certificate' to the response with the '200' status
-  added the optional property 'items/ca_certificate_group' to the response with the '200' status


## PATCH /active-directory/test
-  endpoint added


## POST /data-sealing-keys/revoke
-  endpoint added


## GET /directory-services
-  added the optional property 'items/ca_certificate_group' to the response with the '200' status
-  added the optional property 'items/ca_certificate_group' to the response with the '207' status


## PATCH /directory-services
-  added the new optional request property 'ca_certificate_group'
-  added the optional property 'items/ca_certificate_group' to the response with the '200' status


## POST /directory-services
-  added the new optional request property 'ca_certificate_group'
-  added the new optional request property 'ca_certificate_ref'
-  added the optional property 'items/ca_certificate_group' to the response with the '200' status


## PATCH /directory-services/test
-  added the new optional request property 'ca_certificate_group'


## POST /fleets/members/batch
-  endpoint added


## GET /topology-groups
-  added the new optional 'query' request parameter 'allow_errors'
-  added the success response with the status '207'


## GET /topology-groups/arrays
-  added the new optional 'query' request parameter 'allow_errors'
-  added the success response with the status '207'


## GET /topology-groups/members
-  added the new optional 'query' request parameter 'allow_errors'
-  added the success response with the status '207'


## GET /volumes/diff
- :warning: for the 'query' request parameter 'ids', the maxLength was set to '1'
- :warning: for the 'query' request parameter 'names', the maxLength was set to '1'


