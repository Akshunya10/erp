// Code BY Webdevtrick ( https://webdevtrick.com )
;(function($, window, undefined) {

	'use strict';

	$.ciCalendar = function(options, element) {

		this.$el = $(element);
		this._init(options);

	};

	// set the calendars default options
	$.ciCalendar.defaults = {

		   // array of the different days of the week
		   // 'days' for the full string of each day
		   // '_days' for the abbreviation of each day
		   days : ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
		  _days : ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],

		 // array of the different months of the year
		 // 'months' for the full string of each month
		 // '_months' for the abbreviation of each month
		 months : ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
		_months : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],

		// toggle abbreviations for
		// how days are displayed
		abbr_days: false,

		// toggle abbreviations for
		// how months are displayed
		abbr_months: false,

		// set the left most day in the calendar
		// 0 for sunday, 1 for monday, etc.
		start_day: 0,

		events: {},

		// event handler for when a day (in the current month) is clicked
		dateClick: function($el, $content, dateProperties){ return false; }

	};

	// begin the prototype
	$.ciCalendar.prototype = {

		/*
		 * _init
		 *
		 * Sets the default options into place
		 * and initializes the calendar.
		 *
		 * @param options
		 *
		 */

		_init: function(options) {

			// set the prototype options
			// pulls from defaults unless manually changed
			this.options = $.extend(true, {}, $.ciCalendar.defaults, options);

			// set todays date
			this.today = new Date();

			// set the current month
			this.month = (isNaN(this.options.month) || this.options.month == null) ? this.today.getMonth() : this.options.month - 1;

			// set the current year
			this.year = (isNaN(this.options.year) || this.options.year == null) ? this.today.getFullYear() : this.options.year;

			// set the data array
			this.data = this.options.data || {};

			// generate the calendar template
			this._generate();

			// initialize the events
			this._initEvents();

		},

		/*
		 * _initEvents
		 *
		 * Initializes global events such as
		 * calendar cell clicks.
		 *
		 */

		_initEvents: function() {

			// internalize
			var self = this;

			// handle calendar cell click events
			this.$el.on('click.calendar', 'div.ci-row > div', function() {

				var $cell = $(this),
					idx = $cell.index(),
					$content = $cell.children('div'),
					dateProp = {
						day: $cell.children('span.ci-date').text(),
						month: self.month + 1,
						monthname: self.options.abbr_months ? self.options._months[self.month] : self.options.months[self.month],
						year: self.year,
						weekday: idx + self.options.start_day - 2,
						weekdayname: self.options.days[idx + self.options.start_day - 2]
					};

				if(dateProp.day) {

					self.options.dateClick($cell, $content, dateProp);

				}

			});

		},

		/*
		 * _generate
		 *
		 * Generates a fresh view of the calendar
		 * based on the current year and month.
		 *
		 * @param callback
		 * @return dom
		 *
		 */

		_generate: function(callback) {

			var head = this._getHead(),
				body = this._getDays(),
				rowClass;

			switch(this.rowTotal) {

				case 4 : rowClass = 'cal-rows-four'; break;
				case 5 : rowClass = 'cal-rows-five'; break;
				case 6 : rowClass = 'cal-rows-six'; break;

			}

			this.$cal = $('<div class="ci-calendar ' + rowClass + '">').append(head, body);
			this.$el.find('div.ci-calendar').remove().end().append(this.$cal);

			if(callback) {

				callback.call();

			}

		},

		/*
		 * _getHead
		 *
		 * Generates the weekday strings in the header
		 * of the calendar. Order of weekdays is based
		 * on the options.start_day parameter.
		 *
		 * @return html
		 *
		 */

		_getHead: function() {

			var html =  '<div class="ci-head">';

			for(var i = 0; i <= 6; i++) {

				var pos = i + this.options.start_day,
					j = pos > 6 ? pos - 6 - 1 : pos;

				html += '<div>';
				html += this.options.abbr_days ? this.options._days[j] : this.options._days[j];
				html += '</div>';

			}

			html += '</div>';

			return html;

		},

		/*
		 * _getDays
		 *
		 * Generates the rest of the calendar.
		 * Creates 6 rows, each containing 7 cells.
		 * Cross-checks which day the month starts
		 * and ends on and fills the cells accordingly.
		 *
		 * @return html
		 *
		 */

		_getDays: function() {

			var d = new Date(this.year, this.month + 1, 0),
				monthLength = d.getDate(),
				firstDay = new Date(this.year, this.month, 1);

			// get the starting dat of the month
			this.startingDay = firstDay.getDay();

			// start creating the html output for the calendar cells
			var html = '<div class="ci-body" data-month="' + (this.month + 1) + '"><div class="ci-row" data-week="1">',
				day = 1;

			// loop through the weekdays
			for(var i = 0; i < 7; i++) {

				// add containers for events
				for(var k = 0; k < 2; k++) {

					html += '<span class="ci-event-row" data-event-row="' + (k+1) + '"></span>';

				}

				// loop through week rows
				for(var j = 0; j <= 6; j++) {

					var pos = this.startingDay - this.options.start_day,
						p = pos < 0 ? 6 + pos + 1 : pos,
						inner = '',
						today = this.month === this.today.getMonth() && this.year === this.today.getFullYear() && day === this.today.getDate(),
						content = '';

					if(day <= monthLength && (i > 0 || j >= p)) {

						html += '<div class="' + cellClasses + '" data-month="' + (this.month + 1) + '" data-day="' + day + '" data-events="0">';

						inner += '<span class="ci-date">' + day + '</span>';

						var strdate = (this.month + 1 < 10 ? '0' + (this.month + 1) : this.month + 1) + '-' + (day < 10 ? '0' + day : day) + '-' + this.year,
							dayData = this.data[strdate];

						if(dayData) {

							content = dayData;

						}

						if(content !== '') {

							inner += '<div class="empty">' + content + '</div>';

						}

						++day;

					}else{

						html += '<div class="empty">';

						today = false;

					}

					var cellClasses = today ? 'ci-today ' : '';

					if(content !== '') {

						cellClasses += 'ci-content ';

					}

					html += inner;
					html += '</div>';

				}

				if(day > monthLength) {

					this.rowTotal = i + 1;
					break;

				}else{

					html += '</div><div class="ci-row" data-week="' + (i+2) + '">';

				}

			}

			html += '</div></div>';

			return html;

		},

		/*
		 * _isValidDate
		 *
		 * Referenced from http://stackoverflow.com/a/8390325/989439
		 *
		 * Let's make sure the date being passed through is valid.
		 * Checks day values, month values, leap years, etc.
		 *
		 * @param date
		 * @return array
		 *
		 */

		_isValidDate: function(date) {

			// change date to 'MMDDYYYY' format
			date = date.replace(/-/gi, '');

			// seperate the date string into vars
			var month = parseInt(date.substr(0, 2), 10),
				day   = parseInt(date.substr(2, 4), 10),
				year  = parseInt(date.substr(4, 8), 10);

			// is the month between 1 and 12?
			if((month < 1) || (month > 12)) {

				return false;

			// is the dat between 1 and 31?
			}else if((day < 1) || (day > 31)) {

				return false;

			// there are only 30 days in April, June, September, and November
			}else if(((month == 4) || (month == 6) || (month == 9) || (month == 11)) && (day > 30)) {

				return false;

			// check for leap years
			}else if((month == 2) && (((year % 400) == 0) || ((year % 4) == 0)) && ((year % 100) != 0) && (day > 29)) {

				return false;

			// double check for leap years
			}else if((month == 2) && ((year % 100) == 0) && (day > 29)) {

				return false;

			}

			return {

				day: day,
				month: month,
				year: year

			};

		},

		/*
		 * _clearEvents
		 *
		 * Move the calendar between months and years.
		 * The movement is based on the period and dir
		 * values that are passed into the function.
		 * Period values can be either 'month' or 'year'
		 * and the Dir values 'previous' or 'next'.
		 *
		 */

		_clearEvents: function() {

			$('.ci-event').remove();
			$('.ci-row > div').attr('data-events', 0);

		},

		/*
		 * _updateEvents
		 *
		 * Move the calendar between months and years.
		 * The movement is based on the period and dir
		 * values that are passed into the function.
		 * Period values can be either 'month' or 'year'
		 * and the Dir values 'previous' or 'next'.
		 *
		 * @param array
		 *
		 */

		_updateEvents: function(_events) {

			this._clearEvents();

			// console.log(_events);

			// calculate the number of days between
        	// two supplied dates in mm/dd/yyyy format
            Date.prototype.diffDates = function() {

                var mill = 24 * 60 * 60 * 1000,
                    diff = arguments[0] - this,
                    days = Math.floor(diff/mill);

                return days; // add 1 to include the first day

            }

			// loop through each event supplied in
			// the _events object when the function is called
			$.each(_events, function(index, _event) {

				// define the dom elements we'll need
                var $_event_start_day   = $('.ci-row > div[data-day="' + _event.start['day'] + '"]'),
                	$_event_finish_day  = $('.ci-row > div[data-day="' + _event.end['day'] + '"]'),
                	$_event_start_week  = $_event_start_day.parent(),
                	$_event_finish_week = $_event_finish_day.parent(),
                	$_event_start_cells  = new Array(),
                	$_event_finish_cells  = new Array();

                // define the start date, end date, and number days between them
                var _dateStart  = new Date(_event.start['month'] + '/' + _event.start['day'] + '/' + _event.start['year']),
                    _dateFinish = new Date(_event.end['month'] + '/' + _event.end['day'] + '/' + _event.end['year']),
                    _startPos   = $_event_start_day.index() - 1,
                    _finishPos  = $_event_finish_day.index() - 1,
                    _totalDays  = _dateStart.diffDates(_dateFinish);

                // define the widths of needed elements
                var _blockWidth  = Math.floor($('.ci-row > div').width()), // width of each day in pixels
                	_eventWidth  = _blockWidth * _totalDays, // total width of the event in pixels
                	_eventHeight = Math.floor(($('.ci-event-row').outerHeight() / 2) - 4.5), // get the events height
                	_daysWidth   = _blockWidth * 7, // total width of the calendar in pixels
                	_eventOffset = _startPos * _blockWidth - _blockWidth,
					_eventTotals = _eventWidth + _eventOffset,
					_eventLeftover = _eventTotals - _daysWidth;

				$_event_start_day.addClass('start');

				// make sure the event matches the currently
				// viewed year and month before appending to calendar
                if(_event.start['year'] == calendar.year && _event.start['month'] == calendar.month + 1) {

                	for(var i = _event.start['day']; i <= _event.end['day']; i++){

                		var j = $('.ci-row > div[data-day="' + i + '"]').attr('data-events');

                		j++;

                		$('.ci-row > div[data-day="' + i + '"]').attr('data-events', j);

                	}

                    if(_eventTotals > _daysWidth) {

                    	// this event is long and will carry into the next row

                    	$_event_start_week.find('.ci-event-row').each(function(i, el) {

							$_event_start_cells.push(el);

						});

						$_event_finish_week.find('.ci-event-row').each(function(i, el) {

							$_event_finish_cells.push(el);

						});

                    	var _eventDifference = _eventTotals - _daysWidth,
                    		_eventToDraw = _eventTotals - _eventOffset - _eventDifference;

                		var html_one  = '<span class="ci-event private';
			                html_one += '" style="left:' + (_eventOffset + 6) + 'px;';
			                html_one += 'width:' + (_eventToDraw - _eventHeight - 3) + 'px;">';

			                html_one += '<span class="end-cap" style="';
			                html_one += 'right:-' + Math.floor(_eventHeight/1.5) + 'px; border-width: ' + _eventHeight + 'px 0px ' + _eventHeight + 'px ' + Math.floor(_eventHeight / 1.5) + 'px;';
			                html_one += '"></span>';

			                html_one += '<span class="end-cap-border" style="';
			                html_one += 'right:-' + Math.floor((_eventHeight/1.5) + 2) + 'px; border-width: ' + (_eventHeight + 2) + 'px 0px ' + (_eventHeight + 2) + 'px ' + Math.floor((_eventHeight / 1.5) + 2) + 'px;';
			                html_one += '"></span>';

			                html_one += '<label>' + _event.details['title'] + '<br>starts: ' + _event.start['month'] + '/' + _event.start['day'] + ', ends: ' + _event.end['month'] + '/' + _event.end['day'] + '...</label>';
			                html_one += '</span>';

			            if($_event_start_day.attr('data-events') <= 1) {

		               		$($_event_start_cells[0]).append(html_one);

		               	}else if($_event_start_day.attr('data-events') >= 1) {

		               		$($_event_start_cells[1]).append(html_one);

		               	}else if($_event_start_day.attr('data-events') > 1) {

		               		console.log('view more');

		               	}

			            if(_event.end['month'] === _event.start['month']) {

			            	var html_two  = '<span class="ci-event private';
				                html_two += '" style="left:' + (_eventHeight + 6) + 'px;';
				                html_two += 'width:' + ((_eventDifference - _eventHeight + _blockWidth) - 9) + 'px;">';

				                html_two += '<span class="start-cap" style="';
				                html_two += 'left:-' + Math.floor(_eventHeight/1.5) + 'px; border-width: ' + _eventHeight + 'px ' + Math.floor(_eventHeight / 1.5) + 'px ' + _eventHeight + 'px 0px;';
				                html_two += '"></span>';

				                html_two += '<span class="start-cap-border" style="';
				                html_two += 'left:-' + Math.floor((_eventHeight/1.5) + 2) + 'px; border-width: ' + (_eventHeight + 2) + 'px ' + Math.floor((_eventHeight / 1.5) + 2) + 'px ' + (_eventHeight + 2) + 'px 0px;';
				                html_two += '"></span>';

				                html_two += '<label>...' + _event.details['title'] + '<br>starts: ' + _event.start['month'] + '/' + _event.start['day'] + ', ends: ' + _event.end['month'] + '/' + _event.end['day'] + '</label>';
				                html_two += '</span>';

			  				if($_event_start_day.attr('data-events') <= 1) {

			               		$($_event_finish_cells[0]).append(html_two);

			               	}else if($_event_start_day.attr('data-events') >= 1) {

			               		$($_event_finish_cells[1]).append(html_two);

			               	}else if($_event_start_day.attr('data-events') > 1) {

			               		console.log('view more');

			               	}

			            }

                    }else{

                    	// this event fits within its starting row

                    	$_event_start_week.find('.ci-event-row').each(function(i, el) {

							$_event_start_cells.push(el);

						});

                    	var html  = '<span class="ci-event public';
			                html += '" style="left:' + (_eventOffset + 6) + 'px;';

			                if(_event.start['month'] != _event.end['month']) {

			                	html += 'width:' + (_eventWidth - _eventHeight + _blockWidth - 5) + 'px;">';

			                	html += '<span class="end-cap" style="';
				                html += 'right:-' + Math.floor(_eventHeight/1.5) + 'px; border-width: ' + _eventHeight + 'px 0px ' + _eventHeight + 'px ' + Math.floor(_eventHeight / 1.5) + 'px;';
				                html += '"></span>';

				                html += '<span class="end-cap-border" style="';
				                html += 'right:-' + Math.floor((_eventHeight/1.5) + 2) + 'px; border-width: ' + (_eventHeight + 2) + 'px 0px ' + (_eventHeight + 2) + 'px ' + Math.floor((_eventHeight / 1.5) + 2) + 'px;';
				                html += '"></span>';

			                }else{

			                	html += 'width:' + (_eventWidth + _blockWidth - 5) + 'px;">';

			                }

			                html += '<label>' + _event.details['title'] + '<br>starts: ' + _event.start['month'] + '/' + _event.start['day'] + ', ends: ' + _event.end['month'] + '/' + _event.end['day'] + '</label>';
			                html += '</span>';

			               	if($_event_start_day.attr('data-events') <= 1) {

			               		$($_event_start_cells[0]).append(html);

			               	}else if($_event_start_day.attr('data-events') >= 1) {

			               		$($_event_start_cells[1]).append(html);

			               	}else if($_event_start_day.attr('data-events') > 1) {

			               		console.log('view more');

			               	}

                    }

                }else if(_event.end['year'] == calendar.year && _event.end['month'] == calendar.month + 1) {

                	// this event is being carried over from the previous month

                	$_event_finish_week.find('.ci-event-row').each(function(i, el) {

						$_event_finish_cells.push(el);

					});

					var _newStartPos = _finishPos - _totalDays > 1 ? _finishPos - _totalDays : 1,
						_newStartPos = _newStartPos * _blockWidth - _blockWidth,
						_newEventWidth = _blockWidth * _finishPos - _blockWidth;

					var html  = '<span class="ci-event public';
                        html += '" style="left:' + (_newStartPos + _eventHeight + 6) + 'px;';
                        html += 'width:' + ((_newEventWidth - _eventHeight) - 5) + 'px;">';

                        html += '<span class="start-cap" style="';
                        html += 'left:-' + Math.floor(_eventHeight/1.5) + 'px; border-width: ' + _eventHeight + 'px ' + Math.floor(_eventHeight / 1.5) + 'px ' + _eventHeight + 'px 0px;';
                        html += '"></span>';

                        html += '<span class="start-cap-border" style="';
                        html += 'left:-' + Math.floor((_eventHeight/1.5) + 2) + 'px; border-width: ' + (_eventHeight + 2) + 'px ' + Math.floor((_eventHeight / 1.5) + 2) + 'px ' + (_eventHeight + 2) + 'px 0px;';
                        html += '"></span>';

                        html += '<label>' + _event.details['title'] + '<br>starts: ' + _event.start['month'] + '/' + _event.start['day'] + ', ends: ' + _event.end['month'] + '/' + _event.end['day'] + '</label>';
                        html += '</span>';

                        $($_event_finish_cells[0]).append(html);

                }

			});

		},

		/*
		 * _move
		 *
		 * Move the calendar between months and years.
		 * The movement is based on the period and dir
		 * values that are passed into the function.
		 * Period values can be either 'month' or 'year'
		 * and the Dir values 'previous' or 'next'.
		 *
		 * @param period
		 * @param dir
		 * @param callback
		 *
		 */

		_move: function(period, dir, callback) {

			// take a step back
			if(dir === 'previous') {

				// go back a month
				if(period === 'month') {

					if(this.month > 0) {

						this.month = --this.month;

					}else{

						this.month = 11;
						this.year = --this.year;

					}

				// go back a year
				}else if(period === 'year') {

					this.year = --this.year;

				}

			// put your best foot forward
			}else if(dir === 'next') {

				// go forward a month
				if(period === 'month') {

					if(this.month < 11) {

						this.month = ++this.month;

					}else{

						this.month = 0;
						this.year = ++this.year;

					}

				// go forward a year
				}else if(period === 'year') {

					this.year = ++this.year;

				}

			}

			this._generate(callback);

		},

		/*
		 * _getYear
		 *
		 * Return the current calendar year
		 * @return int
		 *
		 */

		_getYear: function() {

			return this.year;

		},

		/*
		 * _getMonth
		 *
		 * Return the current calendar month
		 * @return int
		 *
		 */

		_getMonth: function() {

			return this.month + 1;

		},

		_getNextMonth: function() {

			var next_month = this.month;

			if(next_month < 11) {

				next_month = ++next_month;

			}else{

				next_month = 0;

			}

			return this.options.abbr_months ? this.options._months[next_month] : this.options.months[next_month];

		},

		_getLastMonth: function() {

			var last_month = this.month;

			if(last_month > 0) {

				last_month = --last_month;

			}else{

				last_month = 11;

			}

			return this.options.abbr_months ? this.options._months[last_month] : this.options.months[last_month];

		},

		/*
		 * _getMonthName
		 *
		 * Return the current calendar month
		 * as a string value. Output will be
		 * determined based on abbreviations
		 * being enabled or disabled.
		 *
		 * @return string
		 *
		 */

		_getMonthName: function() {

			return this.options.abbr_months ? this.options._months[this.month] : this.options.months[this.month];

		},

		_getCell: function(day) {

			var row = Math.floor((day + this.startingDay - this.options.start_day) / 7),
				pos = day + this.startingDay - this.options.start_day - (row * 7) - 1;

			return this.$cal.find('div.ci-body').children('div.ci-row').eq(row).children('div').eq(pos).children('div');

		},

		_setData: function(data) {

			data = data || {};
			$.extend(this.data, data);

			this._generate();

		},

		/*
		 * _gotoNow
		 *
		 * Update the month and year values
		 * to the current date then regenerate
		 * the calendar view.
		 *
		 * @param callback
		 *
		 */

		_gotoNow: function(callback) {

			this.month = this.today.getMonth();
			this.year = this.today.getFullYear();

			this._generate(callback);

		},

		/*
		 * _gotoDate
		 *
		 * Update the calendar to display a
		 * specific month and year based on
		 * the passed values.
		 *
		 * @param month
		 * @param year
		 * @param callback
		 *
		 */

		_gotoDate: function(month, year, callback) {

			this.month = month;
			this.year = year;

			this._generate(callback);

		},

		/*
		 * _gotoNextMonth
		 *
		 * Move the current calendar view
		 * to the upcoming month and then
		 * regenerate the view.
		 *
		 * @param callback
		 *
		 */

		_gotoNextMonth: function(callback) {

			this._move('month', 'next', callback);

		},

		/*
		 * _gotoPreviousMonth
		 *
		 * Move the current calendar view
		 * to the previous month and then
		 * regenerate the view.
		 *
		 * @param callback
		 *
		 */


		_gotoPreviousMonth: function(callback) {

			this._move('month', 'previous', callback);

		},

		/*
		 * _gotoNextYear
		 *
		 * Move the current calendar view
		 * to the upcoming year and then
		 * regenerate the view.
		 *
		 * @param callback
		 *
		 */


		_gotoNextYear: function(callback) {

			this._move('year', 'next', callback);

		},

		/*
		 * _gotoPreviousYear
		 *
		 * Move the current calendar view
		 * to the previous year and then
		 * regenerate the view.
		 *
		 * @param callback
		 *
		 */


		_gotoPreviousYear: function(callback) {

			this._move('year', 'previous', callback);

		}

	};

	/*
	 * _errors
	 *
	 * Basic error logging. Passed errors
	 * are logged through the browser console.
	 *
	 * @param message
	 * @return error
	 *
	 */

	var _errors = function(message) {

		if(window.console) {

			window.console.error(message);

		}

	};

	/*
	 * ciCalendar
	 *
	 *
	 * @param options
	 * @return instance
	 *
	 */

	$.fn.ciCalendar = function(options) {

		// begin a new instance of the calendar
		var instance = $.data(this, 'ciCalendar');

		// if the options being passed into the calendar
		// are in string format, let's go ahead and split
		// it up into a nice shiny array
		if(typeof options == 'string') {

			// shiny new array of arguments
			var args = Array.prototype.slice.call(arguments, 1);

			// loop the arguments
			this.each(function() {

				if(!instance) {

					_errors('cannot call methods on the calendar prior to initialization. ' +
					'attempted to call method "' + options + '"');

					return;

				}

				if(!$.isFunction(instance[options]) || options.charAt(0) === '_') {

					_errors('no such method "' + options + '" for the calendar instance');

					return;

				}

				// valid arguments passed as options
				instance[options].apply(instace, args);

			});

		}else{

			// the options are not being passed as a
			// string. let's parse the passed array
			// and apply them as options

			// loop the arguments
			this.each(function() {

				if(instance) {

					// initialize the existing
					// instance that was passed
					instance._init();

				}else{

					// create a new instance
					// and initialize it afterward
					instance = $.data(this, 'ciCalendar', new $.ciCalendar(options, this));

				}

			});

		}

		return instance;

	};

})(jQuery, window);

var calendar = $('#calendar').ciCalendar({

	dateClick: function($el, $contentEl, dateProperties) {

		console.clear();

		for(var key in dateProperties) {

			console.log(key + ' = ' + dateProperties[key]);

		}

	}

}),

$month = $('#month').html(calendar._getMonthName()),
$year = $('#year').html(calendar._getYear()),
$last = $('#last').html(calendar._getLastMonth()),
$next = $('#next').html(calendar._getNextMonth());


var events = [

	event = {

		details: {

			title: 'Project1',
			location: 'expo center',
			country: 'united states',
			city: 'san diego',
			public: true

		},

		start: {

			time: '12:00pm',
		    month: 5,
		    day: 12,
		    year: 2021,

		},

		end: {

			time: '12:00pm',
		    month: 5,
		    day: 12,
		    year: 2021,

		}

	},

	event = {

		details: {

			title: 'An event that shares days as another event',
			location: 'expo center',
			country: 'united states',
			city: 'san diego',
			public: true

		},

		start: {

			time: '12:00pm',
		    month: 5,
		    day: 24,
		    year: 2021,

		},

		end: {

			time: '12:00pm',
		    month: 5,
		    day: 24,
		    year: 2021,

		}

	},

	event = {

		details: {

			title: 'This is a shorter single row event!',
			location: 'expo center',
			country: 'united states',
			city: 'san diego',
			public: true

		},

		start: {

			time: '12:00pm',
		    month: 8,
		    day: 1,
		    year: 2019,

		},

		end: {

			time: '12:00pm',
		    month: 8,
		    day: 3,
		    year: 2019,

		}

	},

	event = {

		details: {

			title: 'Another short event sharing days',
			location: 'expo center',
			country: 'united states',
			city: 'san diego',
			public: true

		},

		start: {

			time: '12:00pm',
		    month: 8,
		    day: 2,
		    year: 2019,

		},

		end: {

			time: '12:00pm',
		    month: 8,
		    day: 5,
		    year: 2019,

		}

	},

];

calendar._updateEvents(events);

$last.on('click', function() {

	calendar._gotoPreviousMonth(updateMonthYear);

});

$next.on('click', function() {

	calendar._gotoNextMonth(updateMonthYear);

});

$(window).on('resize', function() {

	calendar._updateEvents(events);

});

function updateMonthYear() {

	$month.html(calendar._getMonthName());
	$year.html(calendar._getYear());

	$next.html(calendar._getNextMonth());
	$last.html(calendar._getLastMonth());

	calendar._updateEvents(events);

}