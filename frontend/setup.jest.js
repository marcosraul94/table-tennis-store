import { TextEncoder, TextDecoder } from "util";
import { jest } from "@jest/globals";

Object.assign(global, { TextDecoder, TextEncoder });
