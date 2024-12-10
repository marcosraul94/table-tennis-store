exports.handler = (event, context, callback) => {
  // avoids confirming the user through email
  console.log(event);
  event.response.autoConfirmUser = true;

  callback(null, event);
};
