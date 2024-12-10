exports.handler = (event, context, callback) => {
  // avoids having to send an email to get the confirmation code
  event.response.autoConfirmUser = true;

  callback(null, event);
};
