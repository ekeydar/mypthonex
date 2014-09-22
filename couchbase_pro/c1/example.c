#include <libcouchbase/couchbase.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void error_callback(lcb_t instance,
			   lcb_error_t err,
			   const char *errinfo) {
  printf("Error %s: %s", lcb_strerror(instance, err),
	 errinfo ? errinfo : "");
  exit(EXIT_FAILURE);
}

static void store_callback(lcb_t connection,
                           const void *cookie,
                           lcb_storage_t operation,
                           lcb_error_t error,
                           const lcb_store_resp_t *item) {
  if (error == LCB_SUCCESS) { 
    printf("Rant stored: ");
    fwrite(item->v.v0.key, sizeof(char), item->v.v0.nkey, stdout);
    printf("\n");
  } else {
    printf("Error storing rant: %s (0x%x)\n",
	   lcb_strerror(connection, error), error);
      exit(EXIT_FAILURE);
  }
}


static void get_callback(lcb_t connection,
                         const void *cookie,
                         lcb_error_t error,
                         const lcb_get_resp_t *resp)
{
        if (error != LCB_SUCCESS)
        {
                printf("Error retrieving rant: ");
                fwrite(resp->v.v0.key, 1, resp->v.v0.nkey, stdout);
                printf(" ==> %s\n", lcb_strerror(connection, error));
        }
        else
        {
                printf("Rant retrieved: ");
                fwrite(resp->v.v0.key, 1, resp->v.v0.nkey, stdout);
                printf(" ==> \n");
                fwrite(resp->v.v0.bytes, 1, resp->v.v0.nbytes, stdout);
        }
}

int main(int argc,char** argv) {
  struct lcb_create_st create_options;
  lcb_t connection;
  lcb_error_t err;

  char bucket[2048];
  
  if (argc != 2) {
    printf("Usage: %s <bucket>\n",argv[0]);
    exit(255);
  }
  strcpy(bucket,argv[1]);

  // Set the connection parameters.
  memset(&create_options, 0, sizeof(create_options));
  create_options.v.v0.host = "localhost:8091";
  create_options.v.v0.user = "";
  create_options.v.v0.passwd = "";
  create_options.v.v0.bucket = bucket;

  // Create the connection object with the specified parameters.
  err = lcb_create(&connection, &create_options);
  if (err != LCB_SUCCESS) {
    printf("Error creating instance: %s\n", lcb_strerror(NULL, err));
    exit(EXIT_FAILURE);
  }

  // Set the error handler.
  lcb_set_error_callback(connection, error_callback);
  
  // Set the get operation callback.
  lcb_set_get_callback(connection, get_callback);

  // Set the store operation callback.
  lcb_set_store_callback(connection, store_callback);


  // Connect to Couchbase (asynchronously).
  err = lcb_connect(connection);
  if (err != LCB_SUCCESS) {
    printf("Error initializing connection: %s\n",
	   lcb_strerror(NULL, err));
    exit(EXIT_FAILURE);
  }
  
  // Wait for the connection process to finish.
  lcb_wait(connection);

  // Do stuff.

  // Release the connection.
  lcb_destroy(connection);
  printf("Done - press anything to continue\n");
  getchar();
}

