#!/bin/bash
export DATABASE_URL="postgresql://postgres:7907@localhost:5432/capstone"
export TEST_DATABASE_URI="postgresql://postgres:7907@localhost:5432/test_capstone"

export AUTH0_DOMAIN="fsnp-auth.us.auth0.com"
export ALGORITHMS="RS256"
export API_AUDIENCE="capstone"
export AUTH0_CLIENT_ID="2W4qrLKhF4YON06iM0CiEh24iyc01r1O"

export ASSISTENT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1mRTdtZ2dPaUN0RGxvanhodlpxbiJ9.eyJpc3MiOiJodHRwczovL2ZzbnAtYXV0aC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjIwMjlhNzRjOGU0ZGEwMDY4MmY3ZDBhIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NDQ0MjY2NTgsImV4cCI6MTY0NDUxMzA1OCwiYXpwIjoiMlc0cXJMS2hGNFlPTjA2aU0wQ2lFaDI0aXljMDFyMU8iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3Rvci1pbmZvIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZS1pbmZvIiwiZ2V0Om1vdmllcyJdfQ.h561vx2QbNcvjPLIp-ADqzl__6GgKYEJ5V8DpR6Z7Kmwod9uuAXkBXhIFM7vIpEcKwknXe9Rfi9UO7Q5Fx_yIRIlWKV0JTvvaM0kckX6i854fS29pwrnbl1RCSYN9xpW73q9E9RUkI1OE5ism-TZ799ZR-aCxPFXupyEkDAmZn_cH2n48X2UU2rHxmhADPDDZt6tfTahXy-e5RKKFfdg6Az6vl6g_-99fnNuS0fD-bLO7e3vR6OgUeQsjlHKeyMXi1su4FlRmQAj-7Iz606Aze0is3VJiupe5IerULnGpMdQX6htxJdB5XB8vVhbKaJ-Lj1l7sX8HBnzMjlUpxQWeg"
export DIRECTOR_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1mRTdtZ2dPaUN0RGxvanhodlpxbiJ9.eyJpc3MiOiJodHRwczovL2ZzbnAtYXV0aC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjIwMjk5NTVmNzVhZTcwMDY4ZTBkNTY0IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NDQ0MjY1NDksImV4cCI6MTY0NDUxMjk0OSwiYXpwIjoiMlc0cXJMS2hGNFlPTjA2aU0wQ2lFaDI0aXljMDFyMU8iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3Rvci1pbmZvIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZS1pbmZvIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIl19.JO0RgEihPZsduzLFRInuAQPJkrJ5U7E0qnsBUtbtpUppzbdLiu_7Hbdr2EGNkbx8_QtXT0Z1kgxeMoh8PIezWNu9RRYDMJTOQDv-T44jrt-Wqf1HRznY2_X9aBUaQgbIzPVDIoKIrEQqg20aNyd6VIeqFZPx-vcZf1J-_kdctB876x-i-clIJ22cQ2cZ-q3S7mxYtqYCXwrwLQJ4pUbiaOl2-qMqXhgA6vh2FTplwTTYCRLlgj_9hlgZv4hz65fpFAdWbDzmKznxWQ6_Xu_2pvvA2K2vJCIZNIbtGuPxYucNiLxvwMpD7zzY9WKKBYKe9nytQxEgf4P6k7_6qJU11g"
export PRODUCER_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1mRTdtZ2dPaUN0RGxvanhodlpxbiJ9.eyJpc3MiOiJodHRwczovL2ZzbnAtYXV0aC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmZTVkOTZjZDgwNTUwMDcwZDE1MzA0IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NDQ0MjY0MjYsImV4cCI6MTY0NDUxMjgyNiwiYXpwIjoiMlc0cXJMS2hGNFlPTjA2aU0wQ2lFaDI0aXljMDFyMU8iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3Rvci1pbmZvIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZS1pbmZvIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.kyd0rBETANhVsblg3TjCggDfcmG7K7VAmO-eVJA6QlH2-sRiAa73wetaXhsWIC3vcpkCWEOOErpxXojly9c6o_ubMk_65dVPRqlrdS-ZxvyuWCF1OA9NvJL5EGyn-oiXXSDIBwgfFNFAWeiF6rZ2WH-1aSkKXZ5j50gTpxlWk99ZGhqwM2hKKA3FRJoAdXbRGEj0nRdCiqrPh_jzzQXa87YLS1qNIZ7K05Epyr5WFtyOvvSiN6mFLol26SAo9mWqHE0bB86PF1XK_9I2zOBtr0BzE-qeLK8bKYWAkVcQybwj-vlC95OMHvDGHCcok1GhpjHlf2Js4O9WqE8YrXaG_g"

export EXPIRED_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1mRTdtZ2dPaUN0RGxvanhodlpxbiJ9.eyJpc3MiOiJodHRwczovL2ZzbnAtYXV0aC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmZTVkOTZjZDgwNTUwMDcwZDE1MzA0IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NDQzMzcwNzQsImV4cCI6MTY0NDQyMzQ3NCwiYXpwIjoiMlc0cXJMS2hGNFlPTjA2aU0wQ2lFaDI0aXljMDFyMU8iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3Rvci1pbmZvIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZS1pbmZvIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.OqHXjpJ1HwnFop8K6QNgk3x8Ov1zuLUhISrY2OoSj-PFUVI2xM07kfNGZYAjUluuavibgNeLlr-M69ebfQvVNCBhMZAPHjTce3q4viDQ3FmyuMINfbQgnFP4rugZ1UUmUFugDOC8ffZRBTvbgTJlE3r_A0vDlT2iltEQE5uEpNHLSG9vRqOyU0PwCbFHA1YLuMqvAN6GbP9cBZt0IoGwp12Y5hLj9-XDzV8ssizGRpUS6AnzWkttAtmeH4oyeIg5H4amyISkqizbKRJBuOIO_X2f1-low6BCdzoKey6H7INgwmU8iGWL0I1wVNFwjnEEZRzPVj9Ekrc-gX4WNm1c5w"

export EXCITED="true"

echo "setup.sh script executed successfully!"