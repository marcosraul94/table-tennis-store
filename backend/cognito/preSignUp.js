exports.handler = (event, context, callback) => {
  // avoids confirming the user through email
  event.response.autoConfirmUser = true;

  callback(null, event);
};
