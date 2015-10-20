#!/bin/bash

OUTFILE=$2
CERT=$1
PROXY=""
CURLFLAGS="${PROXY} -k --max-time 15 --connect-timeout 10 --cert ${CERT} -o ${OUTFILE}"
JIRAURL="https://JIRA_SERVER/sr/jira.issueviews:searchrequest-xml/temp/SearchRequest.xml?jqlQuery=%22Active+Participants%22+%3D+CurrentUser%28%29+ORDER+BY+updated+DESC&tempMax=80&field=key&field=summary&field=updated"


curl $CURLFLAGS $JIRAURL
