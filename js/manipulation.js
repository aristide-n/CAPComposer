i = 0;
j = 0;
var $modelInfoBlock,$modelResourceBlock;
/**
 * Storing Form and retrieving it
 * @returns
 */
$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};
		
$(function() {
    $('#infoForm').submit(function() {
    	debugger
    	window.localStorage.setItem("infoForm", JSON.stringify($('#infoForm').serializeObject()));
    	
    });
 });
		
		// What is the next page			
		$(function() {
			$('#backBtn').click(
					function() {
						debugger
        			$("#infoForm").attr('action','./map.html')
					});
					
			$('#nextBtn').click(
					function() {
						debugger
        			$("#infoForm").attr('action','./finish.html')
					});
		});
		
$(function(){
	var resourceIndex = 0;
	var infoForm = localStorage.getItem('infoForm');
	
	if( infoForm != null){
		
		var infoJSON = $.parseJSON(infoForm);
		//Populating the Main Information Block 
		var $block = $('#t1');
		$block.find('.event').val(infoJSON.event[0]);
		$block.find('.category').val(infoJSON.category[0]);
		$block.find('.language').val(infoJSON.language[0]);
		$block.find('.responseType').val(infoJSON.responseType[0]);
		$block.find('.event').val(infoJSON.event[0]);
		$block.find('.severity').val(infoJSON.severity[0]);
		$block.find('.urgency').val(infoJSON.urgency[0]);
		$block.find('.certainty').val(infoJSON.certainty[0]);
		$block.find('.eventCode').val(infoJSON.eventCode[0]);
		$block.find('.senderName').val(infoJSON.senderName[0]);
		$block.find('.headline').val(infoJSON.headline[0]);
		$block.find('.description').val(infoJSON.description[0]);
		$block.find('.instruction').val(infoJSON.instruction[0]);
		$block.find('.web').val(infoJSON.web[0]);
		$block.find('.contact').val(infoJSON.contact[0]);
		$block.find('#count').val(infoJSON.count[0]);
		//$block.find('#resourceList').attr('id','resourceList'+0);
		//$block.find('.arb').attr('data-index',0);
		
		//$block.find('.resourceExpanderHead').attr('id','reh'+0);
		//$block.find('.resourceExpanderHead').attr('data-index',0);
		//$block.find('.resourceExpanderContent').attr('id','rec'+0);
		//$block.find('.resourceExpanderContent').attr('data-index',0);
		
		var count = infoJSON.count[0];
		var infoLength = infoJSON.language.length; 
		var expanderIndex = 1;
		var resourceIndex = 1;
		for(i = 1 ; i < count ; i++){
			var $resourceBlock = $('#resource').clone();
			$resourceBlock.find('.resourceEntry').attr('id','resource'+resourceIndex);
			$resourceBlock.find('.resourceExpanderHead').attr('id','reh'+resourceIndex);
			$resourceBlock.find('.resourceExpanderHead').attr('data-index',resourceIndex);
			$resourceBlock.find('.resourceExpanderContent').attr('id','rec'+resourceIndex);
			$resourceBlock.find('.resourceExpanderContent').attr('data-index',resourceIndex);
			resourceIndex++;
			$resourceBlock.appendTo('#resourceList0');
		}
		$block.appendTo('#listInfo');
		
		for(var i = 1 ; i < infoLength ; i++){
			var $block = $('#t2').clone();
			$block.find('.expanderHead').attr('id','eh'+expanderIndex);
			$block.find('.expanderHead').attr('data-index',expanderIndex);
			$block.find('.expanderContent').attr('id','ec'+expanderIndex);
			$block.find('.expanderContent').attr('data-index',expanderIndex);
			$block.find('.expanderContent').attr('data-index',expanderIndex);
			expanderIndex++;
			$block.find('.event').val(infoJSON.event[i]);
			$block.find('.category').val(infoJSON.category[i]);
			$block.find('.language').val(infoJSON.language[i]);
			$block.find('.responseType').val(infoJSON.responseType[i]);
			$block.find('.event').val(infoJSON.event[i]);
			$block.find('.severity').val(infoJSON.severity[i]);
			$block.find('.urgency').val(infoJSON.urgency[i]);
			$block.find('.certainty').val(infoJSON.certainty[i]);
			$block.find('.eventCode').val(infoJSON.eventCode[i]);
			$block.find('.senderName').val(infoJSON.senderName[i]);
			$block.find('.headline').val(infoJSON.headline[i]);
			$block.find('.description').val(infoJSON.description[i]);
			$block.find('.instruction').val(infoJSON.instruction[i]);
			$block.find('.web').val(infoJSON.web[i]);
			$block.find('.contact').val(infoJSON.contact[i]);
			$block.find('#count').val(infoJSON.count[i]);
			$block.find('#resourceList').attr('id','resourceList'+i);
			$block.find('.arb').attr('data-index',i);
			
			$block.find('.resourceEntry').attr('id','resource'+resourceIndex);
			$block.find('.resourceExpanderHead').attr('id','reh'+resourceIndex);
			$block.find('.resourceExpanderHead').attr('data-index',resourceIndex);
			$block.find('.resourceExpanderContent').attr('id','rec'+resourceIndex);
			$block.find('.resourceExpanderContent').attr('data-index',resourceIndex);
			resourceIndex++;
			$block.appendTo('#listInfo');
			var count = infoJSON.count[i];
			debugger;
			for(var j = 1 ; j < count ; j++){
				var $resourceBlock = $('#resource').clone();
				$resourceBlock.find('.resourceEntry').attr('id','resource'+resourceIndex);
				$resourceBlock.find('.resourceExpanderHead').attr('id','reh'+resourceIndex);
				$resourceBlock.find('.resourceExpanderHead').attr('data-index',resourceIndex);
				$resourceBlock.find('.resourceExpanderContent').attr('id','rec'+resourceIndex);
				$resourceBlock.find('.resourceExpanderContent').attr('data-index',resourceIndex);
				resourceIndex++;
				$resourceBlock.appendTo('#resourceList'+i)
			}
			
		}
		
		
		
 
	}
});
$(document).ready(function(e){
		$("#listInfo").on('click','.expanderHead',function(e){
    		var index = e.currentTarget.getAttribute('data-index');
    		// var $ec = $('.expanderContent')[index];
    		var sliderId = '#ec'+index;
    		$(sliderId).slideToggle();
    		debugger;
    		var sign = e.currentTarget.getElementsByClassName('expanderSign')[0].innerHTML;
    		if ($(sign).attr('class') == "icon-plus-sign"){
    			e.currentTarget.getElementsByClassName('expanderSign')[0].innerHTML = '<i class="icon-minus-sign"></i>';
    		}
    		else {
    			e.currentTarget.getElementsByClassName('expanderSign')[0].innerHTML = '<i class="icon-plus-sign"></i>';
    		}
    	});
		$("#listInfo").on('click','.resourceExpanderHead',function(e){			
			var index = e.currentTarget.getAttribute('data-index');
			var sliderId = '#rec'+index;
			$(sliderId).slideToggle();
			var sign = e.currentTarget.getElementsByClassName('expanderSign')[0].innerHTML;
			if ($(sign).attr('class') == "icon-plus-sign"){
				e.currentTarget.getElementsByClassName('expanderSign')[0].innerHTML = '<i class="icon-minus-sign"></i>';
			}
			else {
				e.currentTarget.getElementsByClassName('expanderSign')[0].innerHTML = '<i class="icon-plus-sign"></i>';
			}
		});
		$("#listInfo").on('click','.arb',function(e){
			var index = e.currentTarget.getAttribute('data-index');
			var $block = $('#resource').clone();
			j++;
			$block.find('.resourceEntry').attr('id','resource'+j);
			$block.find('.resourceExpanderHead').attr('id','reh'+j);
			$block.find('.resourceExpanderHead').attr('data-index',j);
			$block.find('.resourceExpanderContent').attr('id','rec'+j);
			$block.find('.resourceExpanderContent').attr('data-index',j);
			$block.appendTo('#resourceList'+index);
			debugger;
			var count = $('#count'+index).val();
			count++;
			$('#count'+index).val(count);
			console.log('#count' + index+' = '+count);
			return false;
		});
		$('.timepicker-default').timepicker();
		$('.date').datepicker();
});
/**
 * Adds another Info block to the Form!
 */
function addBlock(){
	var $block = $('#t2').clone();
	i++;
	var $expandHead = $block.find('.expanderHead');
	$expandHead.attr('id','eh'+i);
	$expandHead.attr('data-index',i);
	$block.find('.expanderContent').attr('id','ec'+i);
	$block.find('.expanderContent').attr('data-index',i);
	j++;
	$block.find('.arb').attr('data-index',j);
	$block.find('#resourceList').attr('id','resourceList'+j);
	$block.find('#resource').attr('id','resource'+j);
	$block.find('#count').attr('id','count'+j);
	$block.find('.resourceExpanderHead').attr('id','reh'+j);
	$block.find('.resourceExpanderHead').attr('data-index',j);
	$block.find('.resourceExpanderContent').attr('id','rec'+j);
	$block.find('.resourceExpanderContent').attr('data-index',j);
	$block.appendTo('#listInfo');
	console.log('The index value  currently is' + i);
}

    