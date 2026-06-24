from fastapi import FastAPI

#get
#post
#put
#delete
#patch


# 1xx – Informational

# Request received, continue processing.

# 100 Continue → Server received initial request, continue sending.
# 101 Switching Protocols → Server is switching protocol (e.g. HTTP → WebSocket).


# 2xx – Success

# Request was successful.

# 200 OK → Request successful.
# 201 Created → New resource created successfully.
# 202 Accepted → Request accepted, processing later.
# 204 No Content → Request successful, but no response body.

# 3xx – Redirection

# Client must take additional action.

# 301 Moved Permanently → Resource moved permanently to a new URL.
# 302 Found → Temporary redirection.
# 304 Not Modified → Cached version can be used.


# 4xx – Client Errors

# Problem is from the client side (wrong request, unauthorized, etc.)

# 400 Bad Request → Invalid request syntax / missing data.
# 401 Unauthorized → Authentication required.
# 403 Forbidden → Client not allowed to access.
# 404 Not Found → Requested resource not found.
# 405 Method Not Allowed → HTTP method not allowed (e.g. POST on GET-only route).
# 408 Request Timeout → Request took too long.
# 409 Conflict → Conflict with current state (e.g. duplicate entry).
# 415 Unsupported Media Type → Wrong content type.
# 422 Unprocessable Entity → Validation error in data.
# 429 Too Many Requests → Rate limit exceeded.
# Example:
# Wrong API JSON body → 400
# Login token missing → 401
# User has no permission → 403
# Wrong API URL → 404
# Email already exists → 409
# Too many requests → 429


# 5xx – Server Errors

Problem is from the server side.

500 Internal Server Error → Generic server error.
501 Not Implemented → Server doesn’t support requested functionality.
502 Bad Gateway → Invalid response from upstream server.
503 Service Unavailable → Server temporarily unavailable.
504 Gateway Timeout → Upstream server took too long.
Example:
Python backend crashed → 500
Server under maintenance → 503
API gateway timeout → 504